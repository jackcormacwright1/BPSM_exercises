#!/bin/python3

import re

filepath = r'/localdisk/data/BPSM/Lecture18/long_dna.txt'

# ===============================================================
# 1. Read the DNA sequence
# ===============================================================
# A FASTA-style file may start with a header line like ">chr1 ..."
# and may have the sequence split over several lines. We:
#   - skip header lines (those starting with ">")
#   - strip the trailing newline from each sequence line
#   - join the remaining lines into one long string
with open(filepath) as fh:
    dna = ''.join(
        line.strip()
        for line in fh
        if not line.startswith('>')
    )

# Safety clean-up:
#   .upper()          -> make sure lowercase bases become uppercase
#   r'[^ACGT]'        -> "any character that is NOT A, C, G or T"
#   re.sub(..., '', x)-> replace those characters with nothing (= delete them)
dna = re.sub(r'[^ACGT]', '', dna.upper())

# ===============================================================
# 2. Enzyme definitions
# ===============================================================
# Each enzyme maps to (regex-for-site, cut-offset).
#
#   pattern  : regex matching the whole recognition site
#              N = A/C/G/T   ->  [ACGT]
#              R = A/G       ->  [AG]
#              W = A/T       ->  [AT]
#
#   offset   : how many bases from the START of the site the cut
#              happens. Equals the number of characters before the
#              "*" in the notation.
#
#     ANT*AAT  ->  A N T | A A T   ->  offset 3
#     GCRW*TG  ->  G C R W | T G   ->  offset 4
enzymes = {
    "BpsmI":  (r"A[ACGT]TAAT", 3),
    "BpsmII": (r"GC[AG][AT]TG", 4),
}

# ===============================================================
# 3. Which digests to run
# ===============================================================
digests = [
    ("BpsmI single digest",          ["BpsmI"]),
    ("BpsmII single digest",         ["BpsmII"]),
    ("BpsmI + BpsmII double digest", ["BpsmI", "BpsmII"]),
]

# ===============================================================
# 4. Run each digest and print the fragments
# ===============================================================
print('*' * 60)
print(f"Sequence length: {len(dna)} bp")
print('*' * 60)

for criterion, enz_names in digests:

    # ---------- 4a. Collect every cut position -------------------
    cuts = []
    for enz in enz_names:
        pattern, offset = enzymes[enz]

        # The regex "(?=...)" is a "positive lookahead".
        # It matches a POSITION (zero characters) where "pattern"
        # begins, but does NOT consume those characters.
        #
        # Why that matters: plain re.finditer(pattern, dna) resumes
        # the search AFTER the matched block, so overlapping sites
        # are skipped. With lookahead, the search cursor advances
        # only one base at a time, so every start position is seen.
        #
        # Example. Sequence:  A N T A A T A A T
        #   plain finditer("ANTAAT", ...)   -> 1 match (pos 0)
        #   lookahead finditer              -> 1 match (pos 0) here
        #   but for ANT AAT AAT we would see pos 0 only with plain,
        #   whereas overlapping patterns such as ANTAATAAT need the
        #   lookahead to find the second site.
        #
        # m.start()  -> index in `dna` where the site begins.
        # + offset   -> shift to the *cut* position inside the site.
        for m in re.finditer("(?=" + pattern + ")", dna):
            cuts.append(m.start() + offset)

    # ---------- 4b. Convert cut positions to fragments -----------
    # To slice the DNA we need a list of boundaries:
    #
    #    0 ... cut1 ... cut2 ... cut3 ... len(dna)
    #
    #   sorted(set(cuts)) :
    #       set()     removes duplicates — possible when two
    #                 overlapping sites give the same cut, or when
    #                 both enzymes cut at the same index in a
    #                 double digest.
    #       sorted()  puts them in ascending order, required for
    #                 slicing.
    #
    #   [0] + ... + [len(dna)] :
    #       add the ends of the sequence so the first and last
    #       fragments are included.
    bounds = [0] + sorted(set(cuts)) + [len(dna)]

    # Slice between consecutive boundaries.
    #   bounds[i] : bounds[i+1]   for i = 0 .. len(bounds)-2
    # This is the same as pairing consecutive values, but using
    # an index loop instead of zip().
    frags = []
    for i in range(len(bounds) - 1):
        frags.append(dna[bounds[i]:bounds[i + 1]])

    # ---------- 4c. Report ---------------------------------------
    print('-' * 30)
    print(criterion, ':')
    print('  cut sites (0-based):', sorted(cuts))
    print('  number of fragments:', len(frags))
    for i, frag in enumerate(frags):
        print(i, ' ', f'len={len(frag)}', ' ', frag)

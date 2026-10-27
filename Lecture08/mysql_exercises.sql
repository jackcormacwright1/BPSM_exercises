--   mysql -u s1306053 -p -vvv s1306053 < mysql_exercises.sql > mysql_exercises_output.txt

-- Q1. Accession numbers of hits that belong to human
SELECT h.accession
FROM hit_table h
JOIN sequence_table s ON h.sequence_id = s.sequence_id
JOIN sample_table sa  ON s.sample_id   = sa.sample_id
WHERE sa.common_name = 'human';

-- Q2. Recreate the table from the start of the slides (blast_example)
SELECT s.sequence_id     AS sequence_number,
       sa.scientific_name,
       sa.common_name,
       sa.location,
       s.seq             AS sequence,
       s.length,
       h.accession       AS hit_accession,
       h.score           AS hit_score,
       h.length          AS hit_length
FROM sample_table sa
JOIN sequence_table s  ON s.sample_id   = sa.sample_id
LEFT JOIN hit_table h  ON h.sequence_id = s.sequence_id
ORDER BY s.sequence_id, h.blasthit_id;

-- Q3. Sequences longer than 700 bases
SELECT sequence_id, length, seq
FROM sequence_table
WHERE length > 700;

-- Q4. Common names and species names for all samples
SELECT common_name, scientific_name
FROM sample_table;

-- Q5. Accession numbers of hits whose length and score are both > 100
SELECT accession
FROM hit_table
WHERE length > 100 AND score > 100;

-- Q6. DNA of sequences that have a hit with score and length both > 100
--     DISTINCT so a sequence with two such hits is listed once.
SELECT DISTINCT s.sequence_id, s.seq
FROM sequence_table s
JOIN hit_table h ON h.sequence_id = s.sequence_id
WHERE h.score > 100 AND h.length > 100;

-- Q7. HSPs with more than 20 mismatches
SELECT *
FROM blastoutput2
WHERE mismatches > 20;

-- Q8. HSPs shorter than 100 amino acids and with more than 20 mismatches
--     alignment_length is in amino acids here: the subjects are proteins
SELECT *
FROM blastoutput2
WHERE alignment_length < 100 AND mismatches > 20;

-- Q9. First 20 HSPs with fewer than 20 mismatches
--     With no ORDER BY, rows come back in the order they were loaded
SELECT *
FROM blastoutput2
WHERE mismatches < 20
LIMIT 20;

-- Q10. How many HSPs are shorter than 100 amino acids?
SELECT COUNT(*) AS short_hsps
FROM blastoutput2
WHERE alignment_length < 100;

-- Q11. Top ten highest (best) HSPs, by bit score
SELECT *
FROM blastoutput2
ORDER BY bit_score DESC
LIMIT 10;

-- Q12. Start positions of matches whose subject accession contains "AEI"
--      For a case-sensitive match use: LIKE BINARY '%AEI%'
SELECT subject_accession, q_start, s_start
FROM blastoutput2
WHERE subject_accession LIKE '%AEI%';

-- Q13. How many subject sequences have more than one HSP?
--      Inner query: subjects appearing more than once. Outer query: count them.
SELECT COUNT(*) AS subjects_with_multiple_hsps
FROM (SELECT subject_accession
      FROM blastoutput2
      GROUP BY subject_accession
      HAVING COUNT(*) > 1) AS multi;

-- Q14. Percentage of each HSP made up of mismatches
SELECT subject_accession, alignment_length, mismatches,
       ROUND(mismatches / alignment_length * 100, 2) AS percent_mismatch
FROM blastoutput2;

-- Q15. Allocate HSPs into groups by bit score
--      strong >= 200, moderate 50-199, weak < 50 (same bands as the bash/awk version).
SELECT subject_accession, bit_score,
       CASE
         WHEN bit_score >= 200 THEN 'strong'
         WHEN bit_score >= 50  THEN 'moderate'
         ELSE 'weak'
       END AS score_group
FROM blastoutput2;

--      ...and how many HSPs fall in each group
SELECT CASE
         WHEN bit_score >= 200 THEN 'strong'
         WHEN bit_score >= 50  THEN 'moderate'
         ELSE 'weak'
       END AS score_group,
       COUNT(*) AS n_hsps
FROM blastoutput2
GROUP BY score_group;

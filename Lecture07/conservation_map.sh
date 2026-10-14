#!/bin/bash

source config.txt

mkdir -p "${name}"

cp config.txt "${name}/config.txt"

cd "${name}"

echo "Number of threads is set to ${threads}. Press enter to continue or type to override:"
read override

if [[ ${override} != "" ]]; then
	threads=${override}
fi

echo "Running with ${threads} threads."

#dynamically build the query string and esearch
query="${group} AND (${gene}) NOT PARTIAL"
esearch -db protein -query "$query" > search.xml

# extract the count from the search xml to determine whether between 30 and 600
n=$(while IFS='<>/' read -ra line; do if [[ "${line[1]}" == "Count" ]]; then echo "${line[2]}"; fi; done < search.xml)

# if n is empty then esearch failed
if [[ "$n" == "" ]]; then
        echo "No genes found or esearch failed!"
        exit 1
fi

# if less than lower bound warn not enough for pattern
if [[ "$n" -lt "${lower_number_of_genes_allowed}" ]]; then
	echo "Not enough samples for plotting a pattern!"
      	exit 1
fi

# if greater than higher bound warn may be too much processing
if [[ "$n" -gt "${higher_number_of_genes_allowed}" ]]; then
        echo "Too many samples - might take too long to process!"
        exit 1
fi

echo "${n} genes found for ${name}. Fetching FASTA data."
# output in fasta format
efetch -format fasta < search.xml > seqs.fa

#did we download everything the search found?
n_fetched=$(grep -c ">" seqs.fa)
if [[ "$n_fetched" -ne "$n" ]]; then
    echo "Search found ${n} but only ${n_fetched} downloaded!"
    exit 1
fi

# align the samples
clustalo -i seqs.fa -o aligned.fa --force --threads "${threads}"

#same number of sequences out as went in?
n_aligned=$(grep -c ">" aligned.fa)
if [[ "$n_aligned" -ne "$n_fetched" ]]; then
    echo "${n_fetched} sequences went into clustalo but ${n_aligned} came out!"
    exit 1
fi

# plot the conservation chart
plotcon -sequences aligned.fa -winsize "${winsize}" -graph png -goutfile "${name}" 
# use x11 instead of png to output the chart to the graphics interface rather than save as a file

#-s is true if the file exists and isn't empty
if [[ ! -s "${name}.1.png" ]]; then
    echo "plotcon did not make ${name}.1.png!"
    exit 1
fi
echo "Saved ${name}/${name}.1.png"







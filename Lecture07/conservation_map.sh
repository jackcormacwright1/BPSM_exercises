#!/bin/bash

source config.txt

mkdir "${name}"

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

#echo $n

# if less than lower bound warn not enough for pattern
if [[ "$n" -lt "${lower_number_of_genes_allowed}" ]]; then
	echo "Not enough samples for plotting a pattern!"
      	break
# if greater than higher bound warn may be too much processing
elif [[ "$n" -gt "${higher_number_of_genes_allowed}" ]]; then
        echo "Too many samples - might take too long to process!"
        break
else
    echo "${n} genes found for ${name}. Fetching FASTA data."
    # output in fasta format
    efetch -format fasta < search.xml > seqs.fa
    # align the samples
    clustalo -i seqs.fa -o aligned.fa --force --threads "${threads}"
    # plot the conservation charts
    plotcon -sequences aligned.fa -winsize "${winsize}" -graph png -goutfile "${name}" 
fi










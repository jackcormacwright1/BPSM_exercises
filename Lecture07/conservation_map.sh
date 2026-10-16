#!/bin/bash

#--------------------------------------------------------setup
source config.txt

#--------------------------------------------------------name override
echo "Initialising conservation plot pipeline..."
echo
echo "The name of this run is set to ${name}. Press enter to continue or type to override:"
read name_override

if [[ ${name_override} != "" ]]; then
        name=${name_override}
fi

mkdir -p "${name}"

cd "${name}"

echo "Running conservation plot pipeline for ${name}"

#--------------------------------------------------------threads override
echo "Number of threads is set to ${threads}. Press enter to continue or type to override:"
read threads_override

if [[ ${threads_override} != "" ]]; then
        threads=${threads_override}
fi

echo "Running with ${threads} threads."

#--------------------------------------------------------taxonomic group override
echo "Taxonomic group is set to ${group}. Press enter to continue or type to override:"
read group_override

if [[ ${group_override} != "" ]]; then
        group=${group_override}
fi

echo "Running for group ${group}."

#--------------------------------------------------------gene override
echo "Gene is set to ${gene}. Press enter to continue or type to override:"
read gene_override

if [[ ${gene_override} != "" ]]; then
	gene=${gene_override}
fi

echo "Running for gene ${gene}."
echo "This pipeline can run for between ${lower_number_of_genes_allowed} and ${higher_number_of_genes_allowed} genes."
echo "To change this edit the numbers in the config.tx file."

#--------------------------------------------------------winsize override
echo "Window size is set to ${winsize}. Press enter to continue or type to override:"
read winsize_override

if [[ ${winsize_override} != "" ]]; then
        winsize=${winsize_override}
fi

echo "Running for window size ${winsize}."

#--------------------------------------------------------write the config

echo "group=${group}" >> config.txt
echo "winsize=${winsize}" >> config.txt
echo "name=${name}" >> config.txt
echo "gene=${gene}" >> config.txt
echo "higher_number_of_genes_allowed=${higher_number_of_genes_allowed}" >> config.txt
echo "lower_number_of_genes_allowed=${lower_number_of_genes_allowed}" >> config.txt
echo "threads=${threads}" >> config.txt

echo "The variables have been written to a config file in the folder for this run."
echo "The pipeline will now run."

#--------------------------------------------------------esearch
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

#--------------------------------------------------------efetch
echo "${n} genes found for ${name}. Fetching FASTA data."
# output in fasta format
efetch -format fasta < search.xml > seqs.fa

#did we download everything the search found?
n_fetched=$(grep -c ">" seqs.fa)
if [[ "$n_fetched" -ne "$n" ]]; then
    echo "Search found ${n} but only ${n_fetched} downloaded!"
    exit 1
fi

#--------------------------------------------------------alignment
# align the samples
clustalo -i seqs.fa -o aligned.fa --force --threads "${threads}"

#same number of sequences out as went in?
n_aligned=$(grep -c ">" aligned.fa)
if [[ "$n_aligned" -ne "$n_fetched" ]]; then
    echo "${n_fetched} sequences went into clustalo but ${n_aligned} came out!"
    exit 1
fi

#--------------------------------------------------------plotting
# plot the conservation chart
plotcon -sequences aligned.fa -winsize "${winsize}" -graph png -goutfile "${name}" 
# use x11 instead of png to output the chart to the graphics interface rather than save as a file

#-s is true if the file exists and isn't empty
if [[ ! -s "${name}.1.png" ]]; then
    echo "plotcon did not make ${name}.1.png!"
    exit 1
fi
echo
echo "Saved plot to ${name}/${name}.1.png!"







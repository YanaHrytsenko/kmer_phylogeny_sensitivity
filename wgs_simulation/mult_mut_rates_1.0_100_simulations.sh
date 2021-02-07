#!/bin/bash

for rate in 1.0
do
    for i in {1..100};
    do
       mkdir ${rate}_simulation_${i}
       python3 mutate_genome.py $rate Homo_sapiens.GRCh38.dna.chromosome.19_header_line_removed.fa $i # i is the seed to random.seed()
       mv *.txt ${rate}_simulation_${i}
    done
done

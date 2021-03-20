#!/bin/bash

for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
       mkdir ${rate}_simulation_${sim}

       python3 mutate_genome.py $rate Homo_sapiens.GRCh38.dna.chromosome.19.fa $sim # sim is the seed to random.seed() for reproducability
       
       mv *.fa ${rate}_simulation_${sim}
    done
done

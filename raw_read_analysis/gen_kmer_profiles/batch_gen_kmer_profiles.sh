#!/bin/bash

for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
        for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
        do

            path_to_fas_by_sim="/raw_read_analysis/raw_reads_simualtion/generate_illumina_reads/simulated_reads/10X/${rate}_sub_rate/sim_${sim}/"

            python3 gen_kmer_profiles.py $k ${path_to_fas_by_sim}

            kmer_dir="${path_to_fas_by_sim}${k}_mers_mut_rate_${rate}_sim_${sim}/"

            mkdir ${kmer_dir}

            mv *mer_profile.fa ${kmer_dir}

        done
    done
done

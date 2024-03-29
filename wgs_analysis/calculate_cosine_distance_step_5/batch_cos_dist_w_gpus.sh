#!/bin/bash

for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
        for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
        do
            path_to_fas_by_sim=""

            k_mer_dir="${path_to_fas_by_sim}${k}_mers_mut_rate_${rate}_sim_${sim}/"

            sorted_kmers_dir="${k_mer_dir}sorted_${k}_mers_mut_rate_${rate}_sim_$sim"

            kmer_intersection_dir="${sorted_kmers_dir}intersection_FAs_${rate}_mut_rate_${k}_mers/"

            pth=${kmer_intersection_dir}

            if [ ! -f ${pth}${k}_mers_${rate}_mut_rate_${sim}_sim_cos_dist_results.txt ]; then

                FILELIST=( $( find $pth -maxdepth 1 -name "*.txt" |sort) )

                ARRLEN=${#FILELIST[@]}

                for (( i = 0; i < $ARRLEN; i++ ))
                do
                    #1000 is the number of line in a file to process at a time
                    python3 cos_dist_using_gpus.py ${FILELIST[i]} 1000 ${pth}${k}_mers_${rate}_mut_rate_${sim}_sim_cos_dist_results.txt
                done
            fi
        done
    done
done

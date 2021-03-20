#!/bin/bash

for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
        for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
        do
            path_to_fas_by_sim="wgs_analysis/wgs_simulation_step_1/sample_sequences/${rate}_mut_rate/sim_${sim}/"

            k_mer_dir="${path_to_fas_by_sim}${k}_mers_mut_rate_${rate}_sim_${sim}/"

            sorted_kmers_dir="${k_mer_dir}sorted_${k}_mers_mut_rate_${rate}_sim_$sim"

            output_dir="${sorted_kmers_dir}intersection_FAs_${rate}_mut_rate_${k}_mers/"

            mkdir ${output_dir}

            python3 parallel_intersection_of_kmers.py ${sorted_kmers_dir} ${output_dir}

            mv intersection_*.txt ${output_dir}

        done
    done
done

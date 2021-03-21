#!/bin/bash
#Yana Hrytsenko

#module load Python/3.7.4-GCCcore-8.3.0
#module load matplotlib/3.1.1-foss-2019b-Python-3.7.4
#module load scikit-bio/0.5.6-foss-2019b-Python-3.7.4
#module load ete3/3.1.2-foss-2019b-Python-3.7.4


for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
        for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
        do
            dis_file_dir="${rate}_dist_files_all_k_mer_vals/"

            newick_dir="${rate}_mut_rate_all_k_mer_vals/"

            mkdir ${newick_dir}

            newick_out="${newick_dir}${rate}_mut_rate_${k}_mers_sim_${sim}_newick_string.txt"

            dist_file="${dis_file_dir}${k}_mers_${rate}_mut_rate_${sim}_sim_cos_dist_results.txt"

            touch ${newick_out}

            python build_newick_strings.py ${dist_file} >> ${newick_out}

        done
    done
done

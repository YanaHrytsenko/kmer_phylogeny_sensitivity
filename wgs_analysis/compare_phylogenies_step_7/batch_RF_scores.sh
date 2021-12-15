#!/bin/bash

#Yana Hrytsenko

#module load ete3/3.1.2-foss-2019b-Python-3.7.4

for rate in 0.001 0.01 0.1 1.0 10.0
do
    for sim in {1..100};
    do
        for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
        do

          newick_dir=""

          mkdir "CosDist_RF_scores"

          out_dir="CosDist_RF_scores/${k}Mers_RF_scores/"

          mkdir ${out_dir}

          out_file="${k}_mers_${rate}_CosDist_RF_Scores.txt" #will contain all 100 RF scores for 100 simulations per rate per k

          touch ${out_file}

          my_newick_file="${rate}_mut_rate_${k}_mers_sim_${sim}_newick_string.txt"

          python3 calculate_Robinson_Foulds_scores.py ${my_newick_file} >> ${out_file}

        done
    done
done

#!/bin/bash

#Yana Hrytsenko

#module load scipy/1.2.1-foss-2018b-Python-3.7.2

scores_dir="wgs_analysis/compare_phylogenies_step_7/"

for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
do
    python3 calc_RF_score_stats.py ${k} ${scores_dir}CosDist_RF_scores/${k}Mers_RF_scores/ CosDist_sim_WGS_RF_scores_stats.txt
done

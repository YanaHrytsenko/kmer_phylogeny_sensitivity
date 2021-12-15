#!/bin/bash

#Yana Hrytsenko

#module load scipy/1.2.1-foss-2018b-Python-3.7.2



for k in 4 5 6 7 8 9 10 11 12 16
do
    scores_dir=""
    rf_stats_out_dir=""
    python3 calc_RF_scores_statistics.py ${k} ${scores_dir} ${rf_stats_out_dir}CosDist_sim_WGS_RF_scores_stats.txt
done

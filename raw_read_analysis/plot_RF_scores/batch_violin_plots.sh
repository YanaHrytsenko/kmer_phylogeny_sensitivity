#!/bin/bash

#Yana Hrytsenko

#module load matplotlib/3.1.1-foss-2019b-Python-3.7.4


for k in  4 5 6 7 8 9 10 11 12 16
do
    rf_score_dirs=""

    python3 violin_plot_RF_scores.py ${k} ${rf_score_dirs} ${k}_Mers_RF_scores_violin_plot_sim_CosineDist.pdf

done

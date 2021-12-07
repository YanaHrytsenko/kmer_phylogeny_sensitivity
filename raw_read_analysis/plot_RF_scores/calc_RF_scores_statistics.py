#!/usr/bin/env python3
#Yana Hrytsenko

import sys
from scipy import stats
import numpy as np
from statistics import mean, median, stdev


kmer = sys.argv[1]
path_to_score_files = sys.argv[2]
stats_file_out = sys.argv[3]

mut_rates = ['0.001', '0.01', '0.1', '1.0', '10.0']

f = open(stats_file_out, "a")

f.write('\n')

header_line = 'Statistics for ' + kmer + '_Mers: ' + '\n'

f.write(header_line)

divider_line = '==========================' + '\n'

f.write(divider_line)

for i in range(len(mut_rates)):

    rf_scores = np.genfromtxt(path_to_score_files + kmer + '_mers_' + mut_rates[i] + '_RF_Scores.txt', dtype=np.int32)

    stdev_rf = stdev(float(item) for item in list(rf_scores))

    mean_rf = float(mean(list(rf_scores)))

    median_rf = float(median(list(rf_scores)))

    stderr_rf = float(stats.sem(list(rf_scores)))

    subheader_line1 = kmer + '_Mers ' + mut_rates[i] + ' mutation rate: '+ '\n'

    subheader_line2 = 'mean     ' + 'median     ' + 'std_dev        ' + '   std_err    ' + '\n'

    f.write(subheader_line1)

    f.write(subheader_line2)

    stats_line = str(mean_rf) + '       ' + str(median_rf) + '      ' + str(stdev_rf) + '   ' + str(stderr_rf) + '\n'

    f.write(stats_line)

    f.write('\n')


f.close()

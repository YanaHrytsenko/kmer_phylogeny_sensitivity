#!/usr/bin/env python3
#Yana Hrytsenko


import sys
import numpy as np
import matplotlib.pyplot as plt

kmer = sys.argv[1]
output_filename = sys.argv[2]
path_to_score_files = sys.argv[3]

data1 = np.genfromtxt(path_to_score_files + kmer +  '_mers_0.001_RF_Scores.txt', dtype=np.int32)
data2 = np.genfromtxt(path_to_score_files + kmer +  '_mers_0.01_RF_Scores.txt', dtype=np.int32)
data3 = np.genfromtxt(path_to_score_files + kmer +  '_mers_0.1_RF_Scores.txt', dtype=np.int32)
data4 = np.genfromtxt(path_to_score_files + kmer +  '_mers_1.0_RF_Scores.txt', dtype=np.int32)
data5 = np.genfromtxt(path_to_score_files + kmer +  '_mers_10.0_RF_Scores.txt', dtype=np.int32)


data = list([data1, data2, data3, data4, data5])


fig, ax = plt.subplots()


# build a violin plot
ax.violinplot(data, showmeans=False, showmedians=True) #showmeans=True


# add title and axis labels
#ax.set_title(kmer + ' Mers RF scores') no title in the publication
ax.set_xlabel('number of substitutions per site', fontsize = "small")
ax.set_ylabel('Robinson-Foulds score', fontsize = "small")


# add x-tick labels
xticklabels = ['0.00001', '0.0001', '0.001', '0.01', '0.1']
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(xticklabels)


# add horizontal grid lines
ax.yaxis.grid(True)

#store plot in a pdf file
plt.savefig(output_filename, dpi=300.0, format='png')

#show the plot
#plt.show()

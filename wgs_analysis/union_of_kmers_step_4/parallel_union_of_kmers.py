#!/usr/bin/env python3
import sys
import subprocess
from os import listdir
from multiprocessing import Pool

#process union of k_mers in parallel for efficiency

def intersection(f):
    subprocess.call("python3 union_of_kmers.py %s"%(f), shell=True)

directory = sys.argv[1]
files = listdir(directory)

sL = []
usL = []

for item in files:
    if '.fa' in item:
        sL += [item]

s = []
run = []

for i in range(len(sL)):
    for j in range(i+1,len(sL)):
        a = sL[i].split('.fa')
        b = sL[j].split('.fa')

        out = "union_" + a[0] + '_' + b[0] + ".txt"

        run += [directory + "/" + sL[i] + " " + directory + "/" + sL[j] + " " + directory + "/" + out]


pool1 = Pool(processes=50)
pool1.map(intersection,run)

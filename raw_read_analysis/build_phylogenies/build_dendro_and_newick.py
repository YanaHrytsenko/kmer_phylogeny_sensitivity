#!/usr/bin/env python3

#Yana Hrytsenko

#this file containes helper functions for build_newick_strings.py

import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt

def makeUppTMatx(distanceFile, NumberOfsamples, dataFormat):

	distanceFile = open(distanceFile,'r')
	matrix = []
	r = []
	buff = 1
	for line in distanceFile:
		l = line.strip()
		l = l.split(' ')
		if len(r) == int(NumberOfsamples):
			matrix += [r]
			r = []
		if buff != 0 and len(r) == 0:
			i = buff
			while i != 0:
				r += [0]
				i -= 1
			buff += 1
		if (dataFormat == "int"):
			r += [int(l[-1])]
		if (dataFormat == "float"):
			r += [float(l[-1])]
	matrix += [r]
	# make last row
	r = []
	for i in range(NumberOfsamples):
		r += [0]
	matrix += [r]

	distMatrix = np.asarray(matrix)

	distanceFile.close()

	return distMatrix

def makeSymmetricMatx(distanceFile, NumberOfsamples, dataFormat):

	distMatrix = makeUppTMatx(distanceFile, NumberOfsamples, dataFormat)

	for i in range(NumberOfsamples):
	    for j in range(i, NumberOfsamples):
	        distMatrix[j][i] = distMatrix[i][j]

	return distMatrix


def make1DArrayMatx(distanceFile, dataFormat):
    distanceFile = open(distanceFile,'r')
    distances = []
    for line in distanceFile:

        l = line.strip()
        l = l.split(' ')

        if (dataFormat == "int"):
            distances.append(int(l[1]))
			
        if (dataFormat == "float"):
            distances.append(float(l[1]))
    distanceFile.close()

    return distances


def makeDendroWith1DArrayMatx(distances, linkageName, file_name):

    Z = linkage(distances, linkageName)

    fig = plt.figure(figsize=(25, 10))

    dn = dendrogram(Z, labels=list('abcdefgh'))

    plt.savefig(file_name)

    tree = hierarchy.to_tree(Z,False)

    return tree

def getNewick_without_dist(node, newick, leaf_names):

    if node.is_leaf():
        return "%s %s" % (leaf_names[node.id], newick)
    else:
        if len(newick) > 0:
            newick = ")%s" % (newick)
        else:
            newick = ");"

        newick = getNewick_without_dist(node.get_left(), newick, leaf_names)

        newick = getNewick_without_dist(node.get_right(), ",%s" % (newick), leaf_names)

        newick = "(%s" % (newick)


    return newick

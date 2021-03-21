#!/usr/bin/env python3

#Yana Hrytsenko

import sys
from skbio import DistanceMatrix
from skbio.tree import nj
from skbio import TreeNode
from build_dendro_and_newick import makeSymmetricMatx

distanceFile = sys.argv[1]
NumberOfsamples = 8 #number of samples in the tree
dataFormat = "float"

#create symmetrical distance matrix
distMatrix = makeSymmetricMatx(distanceFile, NumberOfsamples, dataFormat)

#names of samples
ids = list('abcdefgh')

#reconstruct phylogeny tree using Neigbour Joining algorithm
dm = DistanceMatrix(distMatrix, ids)
tree = nj(dm)

#build newick tree without distances
no_distances = tree.copy()
for node in no_distances.traverse():
    node.length = None

print(str(no_distances)) #will be printed to a file through bash

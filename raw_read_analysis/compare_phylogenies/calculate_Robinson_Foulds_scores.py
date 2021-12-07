#!/usr/bin/env python3

#Yana Hrytsenko

import sys

# Import ETE Toolkit for visualising tree-based data
from ete3 import Tree

ref_newick = "(((f ,e ),(h ,g )),((d ,c ),(b ,a )));" #known reference tree

my_newick_file = sys.argv[1]

with open(my_newick_file) as f:
    my_newick = f.readline().strip()
f.close()

t1 = Tree(ref_newick)
t2 = Tree(my_newick)

rf_stats = t1.robinson_foulds(t2, unrooted_trees=True)

rf_score = rf_stats[0]

print(rf_score) #will be printed to a file with bash

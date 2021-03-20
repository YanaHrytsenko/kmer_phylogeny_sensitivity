#!/usr/bin/env python3

#Yana Hrytsenko

import os
import sys
import random

def mutate_sequence(origin_sequence, mutation_rate):

    nucleotide_alhabet = ['A', 'T', 'C', 'G']

    result_sequence = origin_sequence[:]

    result_sequence = list(result_sequence)

    for position in range(len(result_sequence)):
        if (result_sequence[position] == 'N'):
            break
        else:
            if (random.uniform(0.0, 1.0) <= (mutation_rate / 100.0 * 1.0)):
                result_sequence[position] = random.choice(nucleotide_alhabet) #pick a random nucleotide from nucleotide_alhabet

    mutated_string = ''.join(result_sequence) #join the list of nucleotides back into string

    return mutated_string


def breed(ref_seq, mutation_rate, height_of_the_tree):

    child1 = ref_seq
    child2 = ref_seq

    child1 = mutate_sequence(child1, mutation_rate)
    child2 = mutate_sequence(child2, mutation_rate)

    if (height_of_the_tree == 0):
        return [child1, child2]
    else:
        return breed(child1, mutation_rate, height_of_the_tree - 1) + breed(child2, mutation_rate, height_of_the_tree - 1)


if __name__ == '__main__':

    mutation_rate = float(sys.argv[1])
    input_file = sys.argv[2] #reference genome file, header line removed
    rand_seed = int(sys.argv[3])

    reference_genome_file = open(input_file,'r')

    original_sequence = ''

    #concatinating genome line by line
    for line in reference_genome_file:
        original_sequence = original_sequence + line.strip()

    reference_genome_file.close()

    random.seed(rand_seed)

    sequence_children = breed(original_sequence, mutation_rate, 2) #log base 2 of 8 = 3 - 1 = 2 levels of the phylogenetic tree

    list_of_out_files = ['a.fa', 'b.fa', 'c.fa', 'd.fa', 'e.fa', 'f.fa', 'g.fa', 'h.fa']


#output each sequence into its .fa file 60bp per line
first_line_of_fa_file = '>19 dna:chromosome chromosome:GRCh38:19:1:58617616:1 REF'

len_of_line_in_fa = 60

for i in range (len(sequence_children)):

    f_out = open(list_of_out_files[i], 'w')

    f_out.write(first_line_of_fa_file + '\n')

    for char in range(0, len(sequence_children[i]) + len_of_line_in_fa, len_of_line_in_fa):

        f_out.write(sequence_children[i][i:i+len_of_line_in_fa] + '\n')

    f_out.close()

i#!/usr/bin/env python3

#Yana Hrytsenko

import os
import sys
import random


def generate_mutation_dict(number_of_mutations, origin_sequence):

    mutation_positions = random.sample(range(len(origin_sequence)-1), number_of_mutations)

    four_nucleotides = ['A', 'T', 'C', 'G']
    mutations = {}

    for position in mutation_positions:

        char_at_position = origin_sequence[position]

        if (char_at_position == 'N'):

            break
        else:
            four_nucleotides_copy = four_nucleotides[:]

            four_nucleotides_copy.remove(char_at_position)

            replacement_nucleotide = four_nucleotides_copy[random.randint(0, len(four_nucleotides_copy)-1)]

            key = position
            value = replacement_nucleotide
            mutations[key] = value

    return mutations

def mutate_sequence(origin_sequence, number_of_mutations):

    mutations = generate_mutation_dict(number_of_mutations, origin_sequence)

    result_sequence = origin_sequence[:]
    result_sequence = list(result_sequence)

    for key in mutations:
        result_sequence[key] = mutations[key]

    mutated_string = ''.join(result_sequence)

    return mutated_string


def breed(chromo_19_ref, number_of_mutations, height_of_the_tree):

    child1 = chromo_19_ref
    child2 = chromo_19_ref

    child1 = mutate_sequence(child1, number_of_mutations)
    child2 = mutate_sequence(child2, number_of_mutations)

    if (height_of_the_tree == 0):
        return [child1, child2]
    else:
        return breed(child1, number_of_mutations, height_of_the_tree - 1) + breed(child2, number_of_mutations, height_of_the_tree - 1)

if __name__ == '__main__':

    mutation_rate = float(sys.argv[1])
    input_file = sys.argv[2] #reference genome file, header line removed
    rand_seed = int(sys.argv[3])

    reference_genome_file = open(input_file,'r')

    original_sequence = ''

    for line in reference_genome_file:
        original_sequence = original_sequence + line.strip()

    reference_genome_file.close()

    number_of_mutations = int((len(original_sequence) * mutation_rate) / 100)



    random.seed(rand_seed)
    sequence_children = breed(original_sequence, number_of_mutations, 2) #log base 2 of 8 = 3, then - 1 (recursion hits two levels, not 3)

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

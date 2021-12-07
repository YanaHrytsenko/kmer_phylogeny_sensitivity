#!/bin/bash

module load Coreutils
module load Python/3.5.2-foss-2016b

for rate in 0.001 0.01 0.1 1.0 10.0
do
   for sim in {1..100};
   do
      for k in 4 5 6 7 8 9 10 11 12 16 21 22 23
      do

         path_to_fas_by_sim="/raw_read_analysis/raw_reads_simualtion/generate_illumina_reads/simulated_reads/10X/${rate}_sub_rate/sim_${sim}/"

         k_mer_dir="${path_to_fas_by_sim}${k}_mers_mut_rate_${rate}_sim_${sim}/"

         bash sortFAs.sh ${k_mer_dir}

         mkdir ${k_mer_dir}sorted_${k}_mers_mut_rate_${rate}_sim_$sim

         mv *_sorted.fa ${k_mer_dir}sorted_${k}_mers_mut_rate_${rate}_sim_$sim

      done
   done
done

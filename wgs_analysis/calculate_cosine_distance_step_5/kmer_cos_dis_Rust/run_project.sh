
module purge
module load Rust/1.42.0-GCCcore-9.3.0

cargo build

for rate in 0.001
do
  for sim in {1..1};
  do
    for k in 4
    do
      
      kmer_intersect_files_dir="/data/schwartzlab/yana/working_w_Rust/kmer_cos_dist/input_files/${k}_mers_${rate}_sim_${sim}/"
      
      pth=${kmer_intersect_files_dir}

      FILELIST=( $( find $pth -maxdepth 1 -name "*.txt" |sort) )

      ARRLEN=${#FILELIST[@]}


      for (( i = 0; i < $ARRLEN; i++ ))
      do
          #python3 cosSimMultGPUs.py ${FILELIST[i]} 1000 ${pth}${k}_mers_${rate}_mut_rate_${sim}_sim_cos_dist_results.txt

          cargo run ${FILELIST[i]} >> output_results_dir/${k}_mers_${rate}_mut_rate_${sim}_sim_CosDist_results.txt
      done
         
    done
  done
done
      

for coverage in 10
do
    for rate in 0.001 0.01 0.1 1.0 10.0
    do
        for sim in {1..10};
        do
            ref_seq_dir="/wgs_analysis/wgs_simulation_step_1/sample_sequences/${rate}_sub_rate/sim_${sim}/"


            read_dir="/raw_read_analysis/raw_reads_simualtion/generate_illumina_reads/simulated_reads/10X/${rate}_sub_rate/sim_${sim}/"


            randomreads.sh ref=${ref_seq_dir}/a.fa out=${read_dir}/single_read_A_set_seed_2_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=2 paired=f

            randomreads.sh ref=${ref_seq_dir}/b.fa out=${read_dir}/single_read_B_set_seed_3_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=3 paired=f

            randomreads.sh ref=${ref_seq_dir}/c.fa out=${read_dir}/single_read_C_set_seed_4_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=4 paired=f

            randomreads.sh ref=${ref_seq_dir}/d.fa out=${read_dir}/single_read_D_set_seed_5_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=5 paired=f

            randomreads.sh ref=${ref_seq_dir}/e.fa out=${read_dir}/single_read_E_set_seed_6_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=6 paired=f

            randomreads.sh ref=${ref_seq_dir}/f.fa out=${read_dir}/single_read_F_set_seed_7_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=7 paired=f

            randomreads.sh ref=${ref_seq_dir}/g.fa out=${read_dir}/single_read_G_set_seed_8_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=8 paired=f

            randomreads.sh ref=${ref_seq_dir}/h.fa out=${read_dir}/single_read_H_set_seed_9_sub_ref_${rate}_${coverage}X.fq length=150 reads=3896041 coverage=10 adderrors=f replacenoref=f simplenames=t seed=9 paired=f

        done
    done
done

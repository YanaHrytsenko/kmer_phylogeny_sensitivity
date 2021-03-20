for coverage in 100
do
    for rate in 0.001
    do
        for sim in {1..1};
        do
            ref_seq_dir="/home/yhrytsenko/whole_genome_sim_diff_mut_rate_project/mut_rate_${rate}_simulations/${rate}_simulation_${sim}/mutation_rate_${rate}_fas_sim_${sim}"

            read_dir="/home/yhrytsenko/sim_reads_diff_mut_rate_project/simulated_reads_data_step_1/simulated_reads_${rate}_mut_rate/finished_simulated_reads_${rate}_rate_${coverage}X_no_errors"
            mkdir ${read_dir}

            randomreads.sh ref=${ref_seq_dir}/a.fa out=${read_dir}/single_read_A_set_seed_2_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=2 paired=f

            randomreads.sh ref=${ref_seq_dir}/b.fa out=${read_dir}/single_read_B_set_seed_3_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=3 paired=f

            randomreads.sh ref=${ref_seq_dir}/c.fa out=${read_dir}/single_read_C_set_seed_4_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=4 paired=f

            randomreads.sh ref=${ref_seq_dir}/d.fa out=${read_dir}/single_read_D_set_seed_5_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=5 paired=f

            randomreads.sh ref=${ref_seq_dir}/e.fa out=${read_dir}/single_read_E_set_seed_6_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=6 paired=f

            randomreads.sh ref=${ref_seq_dir}/f.fa out=${read_dir}/single_read_F_set_seed_7_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=7 paired=f

            randomreads.sh ref=${ref_seq_dir}/g.fa out=${read_dir}/single_read_G_set_seed_8_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=8 paired=f

            randomreads.sh ref=${ref_seq_dir}/h.fa out=${read_dir}/single_read_H_set_seed_9_mut_ref_${rate}_${coverage}X.fq length=150 reads=39078520 coverage=100 adderrors=f replacenoref=f simplenames=t seed=9 paired=f

        done
    done
done

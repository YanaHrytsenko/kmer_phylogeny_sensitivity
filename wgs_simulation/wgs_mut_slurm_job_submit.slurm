#!/bin/bash
#SBATCH --nodes=1
#SBATCH --exclusive

module load Python/3.5.2-foss-2016b

bash mult_mut_rates_0.001_100_simulations.sh

#!/bin/bash

for i in {1..20}
do
    output_file="slurm-job-${i}.sh"
    echo "Creating $output_file..."

    cat <<EOT > $output_file
#!/bin/bash
#SBATCH --account=your_account_name
#SBATCH --gpus-per-node=a100:1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=3
#SBATCH --mem=70G
#SBATCH --time=0-15:00
module load python/3.11.2
module load StdEnv/2020
python gpt-neo-125m-${i}.py

EOT
done


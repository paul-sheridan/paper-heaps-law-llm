#!/bin/bash

# Loop through the generated slurm job scripts and submit them
for i in {2..20}
do
    slurm_file="slurm-job-${i}.sh"
    echo "Submitting $slurm_file..."
    sbatch $slurm_file
done

echo "All jobs submitted."


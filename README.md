# Heaps' Law in GPT-Neo Large Language Model Emulated Corpora
This repository contains computer code for reproducing the results described in the EVIA 2023 Workshop ([landing page](https://research.nii.ac.jp/ntcir/evia2023/)) paper "Heaps' Law in GPT-Neo Large Language Model Emulated Corpora".

Workshop proceedings link: https://research.nii.ac.jp/ntcir/workshop/OnlineProceedings17/EVIA/toc_evia.html

ArXiv preprint link: https://arxiv.org/abs/2311.06377v1


## Getting Started

Clone this repository by running the command
```
git clone https://github.com/paul-sheridan/paper-heaps-law-llm.git
```
and `cd` into the repository root folder `paper-heaps-law-llm`.



## Obtaining the Data

Download the **Pubmed Abstracts** component corpus from The Pile ([download page](https://pile.eleuther.ai/)), an 800GB dataset of diverse text for language modeling.


## Preparing the Environment

Repository code is written in Python 3. It was run on the Narval cluster ([Narval wiki page](https://docs.alliancecan.ca/wiki/Narval/en)), provided by Digital Research Alliance of Canada ([Getting started wiki page](https://docs.alliancecan.ca/wiki/Getting_started)). 

While there are multiple ways to run the repository code, here is one way to do it using Narval:

From the command line, create a virtual environment:
```
virtualenv /project/def-yourName/yourDirectory
```

## Running Repository Code

### Data Selection

In this research we analyze the first 500,000 abstracts in the PubMed Abstracts corpus. To prepare this dataset, run the `dataSelection.py` script:
```
python dataSelection.py
```

To select a custom number of abstracts, navigate to the `dataSelection.py` script and set the `limit` variable on line 8 to be the number of documents that you want to process.

### Data Preprocessing

To preprocess the data according to the steps described in the paper, run:
```
python cleanData.py
```

### Prompt Selection

To choose seed text for abstract emulation, run:
```
python promptSelection.py
```

### Data Genaration

To emulate text from the GPT-Neo models using the above generated seed texts, run the following shell scripts from inside each of the folders `gpt-neo-125m`, `gpt-neo-1.3b`, `gpt-neo-2.7b`:
```
.\generate_python_scripts.sh
.\generate_slurm_scripts.sh
.\submit_all_jobs.sh
```

After that navigate to each folder `gpt-neo-125m`, `gpt-neo-1.3b`, `gpt-neo-2.7b` and run
```
python decode.py
```
This script applies the same preprocesing strageries as used above.


### Heaps' Law Estimation and Visualization

To prepare the emulated texts for analysis, navigate to each folder `gpt-neo-125m`, `gpt-neo-1.3b`, `gpt-neo-2.7b` and run
```
python heapsLaw.py
```

To generate the plots of Figure 1 and Heaps' law parameter estimates of Table 1, run
```
python drawThePlotAndEstimation.py
```



## Citation
If you find anything useful please cite our work using:
```
@inproceedings{Lai2023,
 title = {Heaps' Law in {GPT}-{N}eo Large Language Model Emulated Corpora},
 author = {Lai, Uyen and Randhawa, Gurjit S. and Sheridan, Paul},
 year = {2023},
 note = {NTCIR-17, Track EVIA},
 doi = {10.20736/0002001352}
}
```

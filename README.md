# Heaps' Law in GPT-Neo Large Language Model Emulated Corpora
Official repository for the workshop paper Heaps' Law in GPT-Neo Large Language Model Emulated Corpora
ArXiv preprint link: https://arxiv.org/abs/2311.06377v1

## Getting Started

Clone this repository by running the command
```
git clone https://github.com/paul-sheridan/paper-heaps-law-llm.git
```
and `cd` into the repository root folder `paper-heaps-law-llm`.

## Data


We download the data from The Pile, it is a big data set contain of many small data sets and **PubMed** is one of them.
You can choose whatever dataset you want from here.
https://pile.eleuther.ai/

## Prepare the envinrontment

Repository code is written in Python 3 using Narval Cluster provided by Digital Research Alliance of Canada(https://docs.alliancecan.ca/wiki/Getting_started). 
While there are multiple ways to run a repository, here is one way to do it using Narval:

From the command line, create a virtual environment:

```
virtualenv /project/def-yourName/yourDirctory
```

## Running Repository Code

**DATA SELECTION**
In this research we process 500.000 PubMed documents, so you can navigate to the file and change the amount of document or the document you want to process
```
python dataSelection
```

**Clean Data**
clean the data using the method we mention in the paper
```
python cleanData.py
```

**Promt Selection**
Choose the seed for the LLMs
```
python promtSelection.py
```

**Data Genaration**
Generate data from LLMS using the seed we created.

Navigate to folder gpt-neo-125m, gpt-neo-1.3b, gpt-neo-2.7b.
```
.\generate_python_scripts.sh
.\generate_slurm_scripts.sh
.\submit_all_jobs.sh
```

After that navigate to each folder gpt-neo-125m, gpt-neo-1.3b, gpt-neo-2.7b. and run
```
python decode.py
```
and we use the same cleaning data strageries to clean the data from LLMs

**Heap's law data calculation**
heap's law need number of vocabulary and number of total word in documents so we need to navigate and produce the result use:
```
python heaplaw.py
```

**Heap's law visualization**
generate the plot using
```
python drawThePlotAndEstimation.py
```



****



## Citation
If you find anything useful please cite our work using:
```
@misc{Lai2023,
  author = {Uyen Lai, Gurjit S. Randhawa, Paul Sheridan},
  title = {Heaps' Law in GPT-Neo Large Language Model Emulated Corpora},
  year = {2023},
  eprint = {arXiv:2311.06377v1}
}
```

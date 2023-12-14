# Opinions-Diffusion-Model-Demo

This is a deliverable github repo.
The [https://colab.research.google.com/drive/1JqP6z63uPDY3lyhmwExrEwJuAlANcG8W?usp=sharing]{Google Colab}

## Install
I would suggest in using virtual environment so that allows you to mange separated packages installations for different projects.
**Usage**
```bash
python3 -m venv .venv
source venv/bin/activative
```

I put all the dependent packages within the *requirements.txt* file.
Then, we should install these dependent packages.
```bash
pip3 install -r requirements.txt
```

Once the installations is complete. We can start using tools develop here for better visulized a cycle graph with n-node. And each node are coloring with *"blue"* or *"white"*.



`
Usage: python3 {sys.argv[0]} [--help] | [--nodes] [--steps] [--random_seed] [--model] [--input_file] [--output_file]

These are common commands used in various situations:

start a simple demo, with 20 number of nodes model is "MM" and it takes 5 steps of updates.
    python3 {sys.argv[0]}

start a simple demo, with customized inputs, i.e. number of nodes.
Maximum number of nodes is 30. default is 20. 
    python3 {sys.argv[0]} --nodes=20
    
start a simple demo, with customized input, i.e. number of steps
Maximum number of updating steps is 27. Default is 5.
    python3 {sys.argv[0]} --steps=8

start a simple demo, with customized number of nodes and specified a "RMM" updating rule.
    python3 {sys.argv[0]} --nodes=20 --model="RMM"

start a simple demo, with customized number of nodes and specified a "RMM" updating rule, and specifies a random state.
    python3 {sys.argv[0]} --nodes=20 --model="RMM" --seed=1
`

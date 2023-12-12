import os
import sys
# import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt
import math
from typing import List, Tuple




def Coloring(labels):
  n = len(labels)
  colors = ['']*n
  for idx , i in enumerate(labels):
    if (i == 1):
      colors[idx] = '{}/blue'.format(idx+1)
    else:
      colors[idx] = '{}/white'.format(idx+1)
  print("{" , end = "")
  for j in colors:
    print(j,end = ', ')
  print("}")


def displaying_G(G,coloring,ax = None):
    colors = [""] * len(coloring)
    for idx , label in coloring.items():
        if label == -1:
          colors[idx] = "white"
        elif label == 1:
          colors[idx] = "lightblue"

    nx.draw(G,pos = nx.circular_layout(G) ,ax = ax,with_labels = True, node_color = colors)

def update_node_MM(G,opinions):
  opinions_t = opinions.copy()

  for node in G.nodes():

    # Get agent's neighbors
    neighbors = list(G.neighbors(node))

    # Calculate the majority opinion
    num_positive = sum(opinions[n] == 1 for n in neighbors)

    num_negative = sum(opinions[n] == -1 for n in neighbors)

    if num_positive > num_negative:
        majority_opinion = 1
    elif num_negative > num_positive:
        majority_opinion = -1
    else:
        majority_opinion = opinions[node]

    opinions_t[node] = majority_opinion  # Update agent's opinion
  return opinions_t


def update_node_RMM(G,opinions):
  opinions_t = opinions.copy()

  for node in G.nodes():

    # Get agent's neighbors
    neighbors = list(G.neighbors(node))

    # Calculate the majority opinion
    num_positive = sum(opinions[n] == 1 for n in neighbors)
    # print([opinions[n] == 1 for n in neighbors])

    num_negative = sum(opinions[n] == -1 for n in neighbors)

    if num_positive > num_negative:
        majority_opinion = 1
    elif num_negative > num_positive:
        majority_opinion = -1
    else:
      majority_opinion = (-1) ** (math.ceil(.5-random.random()))

    opinions_t[node] = majority_opinion  # Update agent's opinion
  return opinions_t

 
def read_opinions(fileName) -> List[int]:
    try:
        with open(fileName , 'r') as f:
            for line in f:
                line = line.strip()
                result = [int(e) for e in line.split(',')]
    except ValueError:
        sys.exit("Input Error in input file...")
        
    return result
    
def ini_opinions( num_nodes , fileName = None )->List[int]:
    if fileName == None:
        return [random.choice([1,-1]) for _ in range(num_nodes)]

    return read_opinions(fileName)

def demo(num_steps:int = 5 , num_nodes:int =  20, random_seed:int = 0, model:str = None , input_file:str = None ,output_file = None):
    # Initialize opinions (e.g., +1 or -1) for each node
    # _opinions = [1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1
    # _opinions = [1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,-1]


    # Set the random seed
    if random_seed == None:
        random_seed = 0
    random.seed(random_seed)

    # set the rule of update opinions
    if model == None:
        model = "MM"
    elif model == "MM":
        rule = update_node_MM
    elif model == "RMM":
        rule = update_node_RMM

    # inital the opinions of each node
    _opinions = ini_opinions( num_nodes , input_file )

    # Create a network (graph)
    G = nx.cycle_graph(len(_opinions))


    # opinions = {node: random.choice([-1, 1]) for node in G.nodes()}
    # Mapping opinion to each node
    opinions = {node: _opinions[node] for node in G.nodes()}

    # Number of simulation steps
    num_steps = num_steps


    fig , axs = plt.subplots(3,6,figsize = (11,8.5))
    fig.suptitle(f"Demonstration of {model} Diffusion\n"
                  f"w\ {num_nodes} nodes and {num_steps} steps")
    axs = axs.flatten()
    displaying_G(G,opinions,axs[0])
    axs[0].set_title("Step 0")

    for i, ax in enumerate(axs[1:num_steps+1]):
      opinions = rule(G,opinions)
      displaying_G(G,opinions,ax)
      ax.set_title(f"Step {i+1}")

    for ax in axs[num_steps+1:]:
      plt.delaxes(ax)
    if output_file == None:
        plt.show()
    else: 
        plt.savefig(output_file)

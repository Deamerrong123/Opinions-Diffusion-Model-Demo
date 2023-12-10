import sys
from utils import *
from typing import List, Tuple
import getopt

USAGE = f'''
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
'''
# USAGE = f"Usage: python {sys.argv[0]} [--help] | [-s <sep>] [first [incr]] last"
VERSION = f"{sys.argv[0]} version 1.0.0"

def _vaildModel(s: str)->bool:
    return s in ['MM','RMM']

def _vaildPath(fileName: str)->bool:
    pass


def parse(args: List[str]) -> Tuple[int, int, int, str,str]:
    '''
    Handel command-line interface.
    num_steps   :   set the number of steps for keep track of updating, default 5;
    num_nodes   :   initialize number of nodes, default 20;
    random_seed :   tell about the random state with seed, default 0;
    model       :   tell about the opinions updating rule, "MM" or "RMM", default "MM"
    input_file  :    a file that specifies the opinions of each node, default None if not provided.
    '''
    num_steps = 5
    num_nodes = 20
    random_seed = 0
    model = "MM"
    input_file = None
    options, arguments = getopt.getopt(
        args,                              # Arguments
        "hi:",
        # 'vhs:',                            # Short option definitions
        ["help","steps=", "nodes=", "seed=","model=",'input_file=']) # Long option definitions
    for o, a in options:
        if o in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        elif o in ("--steps"):
            try:
                num_steps = int(a)
            except ValueError:
                raise SystemExit(USAGE)
        elif o in ("--nodes"):
            try:
                num_nodes = int(a)
            except ValueError:
                raise SystemExit(USAGE)
        elif o in ("--seed"):
            try:
                random_seed = int(a)
            except ValueError:
                raise SystemExit(USAGE)
        elif o in ("--model"):
            model = a
        elif o in ("-i","--input_file"):
            input_file = a

    if len(arguments) > 6:
        raise SystemExit(USAGE)

    return num_steps, num_nodes , random_seed , model, input_file

def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)
    num_steps , num_nodes , random_seed , model , input_file = parse(args)
    print(f"You inputs are following: num_steps {num_steps} , num_nodes {num_nodes}, random_seed {random_seed}, model {model},input_file {input_file}\n")

    if (num_nodes > 30):
        sys.exit("Maximum number of nodes is 30! ")
        
    elif num_steps > 28:
        sys.exit("Maximum number of steps is 28! ")

    demo( num_steps , num_nodes, random_seed , model , input_file )

if __name__ == "__main__":
    main()



# if __name__ == "__main__":
#     args = sys.argv[1:] # obtains arguments from CML
#
#     if len(args) > 5:
#         message = "Too much arguments.\n"
#         message += "Usage: "
#         sys.exit(message)
#     
#     demo(num_steps=5,num_nodes=20,rmm = True)
#     # for i , arg in enumerate(args):
#     #     pass

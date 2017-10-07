#!/usr/bin/python

from __future__ import print_function

import sys
import time
import argparse
from utils import print_args
from crystal import Crystal

parser = argparse.ArgumentParser(description="Run commands")
parser.add_argument('-s', '--size', type=int, default=50,
                    help="Size (length) of a 1D-Crystal")
parser.add_argument('-n', '--num-particles', type=int, default=2,
                    help="Number of workers (particles in a crystal)")
parser.add_argument('-p', '--proba', type=float, default=0.5,
                    help="Probability of a particle to move right")
parser.add_argument('-m', '--mode', type=str, default="TIME", choices=["TIME", "ITER"],
                    help="Mode that the program will work in")
parser.add_argument('-t', '--time', type=int, default=60,
                    help="Program execution time limit in seconds")
parser.add_argument('-d', '--delay', type=int, default=100,
                    help="Time each particle will sleep between iterations in milliseconds")
parser.add_argument('-i', '--num_iters', type=int, default=100,
                    help="Maximum number of iterations each particle does")

parser.add_argument('--visualise', action='store_true',
                    help="Visualise a crystal to see positions of particles")


def run_crystal(args):
    print ("Crystal is running ", end='')
    sys.stdout.flush()

    for i in range(10):
        print ('.', end='')
        sys.stdout.flush()
        time.sleep (200.0 / 1000.0)

    print ()

    crystal = Crystal(args.size, args.num_particles, args.proba,
                      args.time, args.delay, args.num_iters)
    crystal.run(args.visualise)

    print ("Finished!")


if __name__ == "__main__":
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if (args.mode == "TIME"):
        args.num_iters = -1
    else:
        args.time = -1
        args.delay = 0

    print_args(args)
    run_crystal(args)

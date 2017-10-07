#!/usr/bin/python

from __future__ import print_function

sign_repeat = 40

def print_args(args):

    timelimit = str(args.time) if args.time > 0 else "-1 (UNLIMITED)"
    iters = str(args.num_iters) if args.num_iters > 0 else "-1 (UNLIMITED)"
    delay = str(args.delay) if args.delay > 0 else "0"

    print ("=" * sign_repeat)
    print ("The next crystal parameters will be used:")
    print ("=" * sign_repeat)
    print ("Size of the crystal: ", args.size)
    print ("Number of particles: ", args.num_particles)
    print ("Proba: ", args.proba)
    print ("Time limit: ", timelimit)
    print ("Iteration delay: ", delay)
    print ("Number of iterations: ", iters)
    print ("=" * sign_repeat)
    print ()

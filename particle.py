#!/usr/bin/python

from __future__ import print_function

import time
import random
import threading

class Particle(threading.Thread):
    def __init__(self, p_index, size, position, positions,
                 condition, proba, delay, num_iters):
        threading.Thread.__init__(self)
        self.p_index = p_index
        self.size = size
        self.position = position
        self.positions = positions
        self.condition = condition
        self.proba = proba
        self.delay = delay
        self.num_iters = num_iters
        self.iteration = 0

        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            if self.iteration == self.num_iters:
                self.stop()

            ## ====== DO A STEP [START] ====== #
            if self.position == 0:
                self.position += 1
            elif self.position == self.size - 1:
                self.position -= 1
            else:
                # +1 to move right or -1 to move left
                self.position += \
                    2 * int(random.random() < self.proba) - 1

            # Update global memory with the current position
            with self.condition:
                self.positions[self.p_index] = self.position
            ## ====== DO A STEP [END]  ====== #

            if self.num_iters > 0:
                self.iteration += 1
            else:
                time.sleep (self.delay / 1000.0)

    def stop(self):
        self.stop_event.set()

    def is_stopped(self):
        return self.stop_event.is_set()

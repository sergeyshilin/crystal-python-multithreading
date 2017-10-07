#!/usr/bin/python

from __future__ import print_function

import time
import curses
import threading

from particle import Particle

class Crystal:

    visualization_delay = 300

    def __init__(self, size, num_particles, proba, time_limit, delay, num_iters):
        self.size = size
        self.num_particles = num_particles
        self.proba = proba
        self.time_limit = time_limit
        self.num_iters = num_iters
        self.delay = delay
        self.positions = [0 for _ in range(num_particles)]

        self.update_position_cond = threading.Condition()

        self.particles = [Particle(i, size, 0, self.positions, self.update_position_cond,
                            proba, delay, num_iters) for i in range(num_particles)]

    def start_particles(self):
        for p in self.particles:
            p.start()

    def join_particles(self):
        for p in self.particles:
            p.join()

    def stop_particles(self):
        for p in self.particles:
            p.stop()

    def is_running(self):
        num_in_progress = 0

        for p in self.particles:
            if not p.is_stopped():
                num_in_progress += 1

        return num_in_progress != 0

    def print_current_state(self, window):
        for p in range(self.num_particles):
            out_str = "[{0: <2}] {1}*{2}".format(p + 1, "-" * self.positions[p], '-' * (self.size - 1 - self.positions[p]))
            window.addstr(p, 0, out_str)
            
        window.refresh()

    def run(self, visualise):
        start_time = time.time()
        self.start_particles()

        ## === INIT VISUALIZATION === ##
        if visualise:
            window = curses.initscr()
            curses.noecho()
            curses.cbreak()
        ## === INIT VISUALIZATION === ##

        while self.is_running():
            if self.num_iters < 0:
                if time.time() - start_time > self.time_limit:
                    self.stop_particles()

            if visualise:
                self.print_current_state(window)

            time.sleep(Crystal.visualization_delay / 1000.0)

        ## === STOP VISUALIZATION === ##
        if visualise:
            curses.echo()
            curses.nocbreak()
            curses.endwin()
        ## === STOP VISUALIZATION === ##

        self.join_particles()

        print ("Last crystal state: ",
            *zip([i + 1 for i in range(self.num_particles)], self.positions))

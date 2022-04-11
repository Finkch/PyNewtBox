"""
Skyler A. is the Galactic Overlord of this code.
    This iteration was started on March 10, 2022.
    The goal of this code is to reasonably accurately simulate and display celestial bodies in their dance of
        gravitational forces.
    Mostly to look good rather than calculate anything meaningful.

    As a note, all measurements and outputs are in SI units unless otherwise specified
"""

# The required imports
import ActorProperties as ap
import Calculations as calc
import Constants as cons
import Planets as pl
import time as tm
import Utility as util
import Stopwatch


#   Contains the primary simulation loop
def exist(actors, time):

    #   Defines whether the universe is or isn't
    exists = True
    steps = 0

    real_time = Stopwatch.Stopwatch(5)


    #   Simulates
    while exists:

        #   Handles the stopwatches
        real_time.push_time()


        #   Cleans a few things up after every step
        tm.sleep(0.5)
        util.cls()


        #   Applies gravitational forces to each actor
        calc.gravity(actors)


        #   A basic time tracker
        print("Steps:", steps, "\tTime per step:", time, "\tTime simulated:", (steps * time), "s\tSimulation rate:", util.round_str(time / real_time.peek_delta()) + "x")
        print("Time taken on step:", util.round_str(real_time.peek_delta()), "s\tTotal elapsed time:", util.round_str(real_time.since_start()), "s")


        #   Moves an actor in space
        for actor in actors:
            actor.update_space(time)

            #   Prints a summary for each actor
            print(actor)

        steps += 1


# This class initialises the universe
def startup():

    #   Creates the list of actors and populates it
    actors = []
    sol = pl.sol
    terra = pl.terra
    terra.pos.x = cons.AU

    #   Gives the actors some velocity
    terra.velo = ap.Vector(0, 1e4, 1e4)


    actors.append(sol)
    actors.append(terra)


    #   Defines the ratio of seconds to step
    time = 1

    #   Enters the simulation
    exist(actors, time)


#   In the beginning, there was nothing
#   Then, God said "startup()"
startup()

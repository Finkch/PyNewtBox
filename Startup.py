"""
Skyler A. is the Galactic Overlord of this code.
    This iteration was started on March 10, 2022.
    The goal of this code is to reasonably accurately simulate and display celestial bodies in their dance of
        gravitational forces.
    Mostly to look good rather than calculate anything meaningful.

    As a note, all measurements and outputs are in SI units unless otherwise specified
"""

# The required imports
#import ActorProperties as ap
import Calculations as calc
import Constants as cons
import Planets as pl
import Utility as util
import Deque
import States as st


#   Contains the primary simulation loop
def exist(actors, time):

    #   Defines whether the universe is or isn't
    exists = True
    steps = 0

    real_time = Deque.Stopwatch(5)
    frame_time = Deque.Stopwatch(5)
    real_time.push_time()
    frame_time.push_time()

    #   Stores the worldlines
    states = st.State()

    #   The Debugger handles printing things to console
    debugger = Deque.Debugger()
    debugger.add_tags([
        "actor",
        "sim_time",
        "real_time"
    ])


    #   Simulates
    while exists:

        #   Handles the stopwatches
        real_time.push_time()
        next_frame = frame_time.since() > 1 / 15


        #   Applies gravitational forces to each actor
        calc.gravity(actors)

        #   Moves an actor in space & adds the state
        for actor in actors:
            actor.update_space(time)
            states.add(steps * time, actors)


        #   When enough time has passed for the next frame to be drawn
        #       Pushes relevant information to console & prints it
        if next_frame:
            util.cls()

            #   Retrieves the current state
            current_state = states.get(steps * time)

            #   Pushes everything to the debugger
            for actor in current_state:
                debugger.push(actor, "actor", next_frame)
            debugger.push("Time taken on step: " + util.round_str(real_time.peek_delta()) + " s\tTotal elapsed time: " + util.round_str(real_time.since_start()) + " s\tFramerate: " + "{:.2f}".format(1 / frame_time.since()) + " fps", "real_time", next_frame)
            debugger.push("Steps: " + str(steps) + "\tTime simulated: " + util.seconds_to_clock(steps * time) + "\tTime per step: " + str(time) + " s\tSimulation rate:" + util.round_str(time / real_time.peek_delta()) + "x", "sim_time", next_frame)

            #   Pops the debugger until it is empty
            while not debugger.is_empty():
                print(debugger.pop())

            #   Updates the stopwatch in charge of framerate
            frame_time.push_time()

        #   Increments the step
        steps += 1


# This class initialises the universe
def startup():

    #   Creates the list of actors and populates it
    actors = []
    sol = pl.sol

    terra = pl.terra
    terra.pos.x = cons.AU
    terra.velo.y = 30220

    luna = pl.luna
    luna.pos.x = cons.AU + cons.LU
    luna.velo.y = 1.022e3 + terra.velo.y

    actors.append(sol)
    actors.append(terra)
    #actors.append(luna)


    #   Defines the ratio of seconds to step
    time = 1

    #   Enters the simulation
    exist(actors, time)


#   In the beginning, there was nothing
#   Then, God said "startup()"
startup()

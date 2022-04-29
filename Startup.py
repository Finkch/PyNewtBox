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
import Plotter


#   Does one step of simulation
def simulate(actors, states, steps, time):
    #   Applies gravitational forces to each actor
    calc.gravity(actors)

    #   Updates each actor based on their acceleration
    for actor in actors:
        actor.update_space(time)
        states.add(steps * time, actors)


#   Contains the primary simulation loop
def exist(actors):

    #   Defines whether the universe is or isn't
    exists = True

    #   Defines the ratio of seconds to step
    time = 0.1

    #   The steps simulated vs. the steps shown
    steps = 0
    sim_steps = 0


    #   Creates the plotter
    plotter = Plotter.Plotter()

    #   Starts the stopwatches
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
        "real_time",
        "frame_time"
    ])


    #   Simulates
    while exists:

        #   Handles the stopwatches
        real_time.push_time()
        next_frame = frame_time.since() > 1 / 15


        #   Moves an actor in space & adds the state
        simulate(actors, states, steps, time)


        #   When enough time has passed for the next frame to be drawn
        #       Pushes relevant information to console & prints it
        if next_frame:
            util.cls()

            #   Retrieves the current state
            timestamp = round(real_time.since_start(), 1)
            current_state = states.get(timestamp)


            #   Draws the current state
            plotter.draw(current_state)

            #   Pushes the current state to the debugger
            for actor in current_state:
                debugger.push(actor, "actor", next_frame)
            debugger.push("Time taken on step: " + util.round_str(real_time.peek_delta()) + " s\tTotal elapsed time: " + util.seconds_to_clock(real_time.since_start()) + " s\tFramerate: " + "{:.2f}".format(1 / frame_time.since()) + " fps", "frame_time", next_frame)
            debugger.push("Current step: " + str(timestamp // time) + "\tCurrent time: " + util.seconds_to_clock(timestamp) + " s\tStep delta: " + util.round_str(steps - sim_steps), "real_time", next_frame)
            debugger.push("Steps: " + str(steps) + "\tTotal time simulated: " + util.seconds_to_clock(steps * time) + "\tTime per step: " + str(time) + " s\tSimulation rate:" + util.round_str(time / real_time.peek_delta()) + "x", "sim_time", next_frame)

            #   Pops the debugger until it is empty
            while not debugger.is_empty():
                print(debugger.pop())


            #   Updates the stopwatch in charge of framerate
            frame_time.push_time()
            sim_steps += 1

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

    #   Enters the simulation
    exist(actors)


#   In the beginning, there was nothing
#   Then, god said "startup()"
startup()

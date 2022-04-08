"""
Skyler A. is the Galactic Overlord of this code.
    This iteration was started on March 10, 2022.
    The goal of this code is to reasonably accurately simulate and display celestial bodies in their dance of
        gravitational forces.
    Mostly to look good rather than calculate anything meaningful.
"""

# The required imports
import ActorProperties as ap
import Calculations as calc
import Constants as cons


# This class initialises the universe
def startup():

    actors = []
    sol = ap.Actor("Sol", 1e30, 1)
    terra = ap.Actor("Terra", 1e30, 1)
    sol.pos.x = 1

    actors.append(sol)
    actors.append(terra)

    calc.gravity(actors)

    for actor in actors:
        actor.update_space(1)

    print(sol)
    print(terra)

startup()

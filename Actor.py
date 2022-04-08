# An actor is a class that contains all the information required to model a celestial body
#   That is, at least in terms of its orbit
#   An actor is defined by its mass and radius
#   It is modelled in two ways:
#     Gravitationally, it is a point mass
#     Volume-wise, it is a perfect sphere

class Actor:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
#   A vector contains magnitude and direction
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + "\ty: " + str(self.y) + "\tz: " + str(self.z)

    #   Returns the quadrature sum
    def get_mag(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)

    #   Returns the unit vector in the same direction as this vector
    def get_normal(self):
        mag = self.get_mag()
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    #   Add the inputted vector to this vector
    def add(self, add_vec):
        self.x += add_vec.x
        self.y += add_vec.y
        self.z += add_vec.z

    # Adds a vector multiplied by a scalar
    def add_mult(self, add_vec, scalar):
        self.x += add_vec.x * scalar
        self.y += add_vec.y * scalar
        self.z += add_vec.z * scalar


# An actor is a class that contains all the information required to model a celestial body
#   That is, at least in terms of its orbit
#   An actor is defined by its mass and radius
#   It is modelled in two ways:
#     Gravitationally, it is a point mass
#     Volume-wise, it is a perfect sphere
class Actor:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius

        self.pos = Vector(0, 0, 0)
        self.velo = Vector(0, 0, 0)
        self.accel = Vector(0, 0, 0)

    def __str__(self):
        return self.name + "\n\tMass:\t" + str(self.mass) + "\n\tRadius:\t" + str(self.radius) + "\n\tpos:\t" + str(self.pos) + "\n\tvelo:\t" + str(self.velo) + "\n\taccel:\t" + str(self.accel)

    #   Updates the actor's...
    #       Velocity, based on its acceleration
    #       Position, based on its velocity
    #       And it's acceleration back to zero
    def update_space(self, time):
        self.velo.add_mult(self.accel, time)
        self.pos.add_mult(self.velo, time)

        #   If a debugger is implemented, here is where it would push vectors

        self.accel = Vector(0, 0, 0)

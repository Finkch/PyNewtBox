# A vector describes direction and magnitude in 3-space; x, y, & z
#   Their goal is to package together the important information within a single vector

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Returns the quadrature sum
    def getMagnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)

    # Returns the unit vector in the same direction as this vector
    def getNormal(self):
        mag = self.getMagnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag)
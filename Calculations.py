#   This file handles most of the simple calculations

import ActorProperties as ap
import Constants as cons

#   Applies gravity between each actor
def gravity(actor_list):
    for i in range(0, len(actor_list)):
        for j in range((i + 1), len(actor_list)):
            if actor_list[i] != actor_list[j]:
                dist = vector_difference(actor_list[i].pos, actor_list[j].pos)
                mag = dist.get_mag()

                first_force = cons.G * actor_list[j].mass / (mag ** 2)
                second_force = cons.G * actor_list[i].mass / (mag ** 2)

                first_normal = dist.get_normal()
                second_normal = ap.Vector(-1 * first_normal.x, -1 * first_normal.y, -1 * first_normal.z)

                first_accel = ap.Vector(first_force * first_normal.x, first_force * first_normal.y, first_force * first_normal.z)
                second_accel = ap.Vector(second_force * second_normal.x, second_force * second_normal.y, second_force * second_normal.z)

                actor_list[i].accel.add(first_accel)
                actor_list[j].accel.add(second_accel)




#   Returns the difference between two vectors
#       second_vector - first_vector
def vector_difference(first_vector, second_vector):
    return ap.Vector(second_vector.x - first_vector.x,
                     second_vector.y - first_vector.y,
                     second_vector.z - first_vector.z)

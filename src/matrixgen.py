import numpy as np
import matrix
from random import randint
from math import log, sqrt


class MatrixGen():

    wall1 = np.matrix('0, 1;\
                       1, 1;\
                       1, 0'.rstrip())

    wall2 = np.array('1, 0;\
                      1, 1;\
                      0, 1'.rstrip())

    wall3 = np.array('1, 1, 1, 1')

    wall4 = np.array('1;\
                      1;\
                      1;\
                      1'.rstrip())

    wall_list = [wall1, wall2, wall3, wall4]


    def __init__(self):
        pass

    def gen_mat(self, width, height):
        if not width or not height:
            return None

        width=int(width)
        height=int(height)

        mat = np.zeros((width, height), dtype=int)

        min_amount_walls = int(log(sqrt(width * height)))
        max_amount_walls = int(log(sqrt(width * height)) * 2)
        final_mat = self.add_walls(mat, min_amount_walls, max_amount_walls)

        mat_obj = Matrix(width, height, final_mat)

        return mat_obj

    """
    adds a random amount of walls from wall_lis to an existing matrix and returns it
    the amount of walls is in a range between the minimum amount of walls and
    maximum amount of walls passed over to the function
    """
    def add_walls(self, mat, min_w, max_w):
        # create a random amount of walls in a range of the minimum amount
        # of walls and the maximum amount of walls
        for i in range(0, randint(min_w, max_w)):
            coord = Coordinate.gen_rand_coord()

            # grab a random wall from the list
            wall = wall_list[randint(0, len(wall_list))]

            mat = replace_with_wall(mat, coord.x, coord.y, wall)
        return mat

    def replace_with_wall(self, mat, x, y, wall):
        wall_width = wall.shape[0]
        wall_height = wall.shape[1]

        from_x = x
        from_y = y

        # coordinate for wall + wall dimensions to create a replaceable shape in the matrix
        to_x = wall.shape[0] + x
        to_y = wall.shape[1] + y

        """
        We have to move our wall back inside if the coordinates specified make
        it poke out like in the graphic below

        WALL: X |
              X X
              | X

        | | | | | | | | | |        | | | | | | | | | |
        | | | | | | | | | |        | | | | | | | | | |
        | | | | | | | | | |        | | | | | | | | | |
        | | | | | | | | | |  --->  | | | | | | | | | |
        | | | | | | | | | |        | | | | | | | | X |
        | | | | | | | | | X        | | | | | | | | X X
        | | | | | | | | | X X      | | | | | | | | | X
                            X
        """
        # if the wall would go out of bounds by width
        if to_x > mat.shape[0]:
            # reduce from_x and to_x by the same amount to make it fit
            from_x -= wall_width
            to_x -= wall_width

        # if the wall would go out of bounds by height
        if to_y > mat.shape[1]:
            from_y -= wall_height
            to_y -= wall_height

        # actually replace the wall now
        mat[from_x:to_x, from_y:to_y] = wall

        return mat

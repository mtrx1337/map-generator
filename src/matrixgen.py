import numpy as np
from matrix import Matrix
from coordinate import Coordinate
from random import randint
from math import log, sqrt


class MatrixGen():

    rm = lambda x : x.strip("\n").strip(" ")

    '''
    [[0, 1]
     [1, 1]
     [1, 0]]
    '''
    wall1 = [[0, 1],[1, 1],[1, 0]]

    '''
    [[1, 0]
     [1, 1]
     [0, 1]]
    '''
    wall2 = [[1, 0],[1, 1],[0, 1]]

    '''
    [1, 1, 1, 1]
    '''
    wall3 = [1, 1, 1, 1]

    '''
     [[1]
      [1]
      [1]
      [1]]
    '''
    wall4 = [[1],[1],[1],[1]]

    wall_list = [wall1, wall2, wall3, wall4]


    def __init__(self):
        pass

    def gen_mat(self, size):
        if not size:
            return None

        width=int(size)
        height=int(size)

        mat = np.zeros((width, height), dtype=int).tolist()

        min_amount_walls = int(log(sqrt(width * height)))
        max_amount_walls = int(log(sqrt(width * height)) * 2)
        final_mat = self.add_walls(mat, width, min_amount_walls, max_amount_walls)

        mat_obj = Matrix(width, final_mat)

        return mat_obj

    """
    adds a random amount of walls from wall_lis to an existing matrix and returns it
    the amount of walls is in a range between the minimum amount of walls and
    maximum amount of walls passed over to the function
    """
    def add_walls(self, mat, width, min_w, max_w):
        # create a random amount of walls in a range of the minimum amount
        # of walls and the maximum amount of walls
        for i in range(0, randint(min_w, max_w)):
            coord = Coordinate()
            coord.gen_rand_coord(width)

            # grab a random wall from the list
            wall = self.wall_list[randint(0, len(self.wall_list) - 1)]

            mat = self.replace_with_wall(mat, coord.x, coord.y, wall)
        return mat

    def replace_with_wall(self, mat, x, y, wall):
        # if wall is one dimensional, don't try to get the size of the second dimension
        wall_width = 1
        wall_height = 1
        if type(wall[0]) is not int:
            wall_width = len(wall[0])
        if type(wall) is not int:
            wall_height = len(wall)

        from_x = x
        from_y = y

        # coordinate for wall + wall dimensions to create a replaceable shape in the matrix
        to_x = wall_width + x
        to_y = wall_height + y

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
        if to_x > wall_width:
            # reduce from_x and to_x by the same amount to make it fit
            from_x -= wall_width
            to_x -= wall_width

        # if the wall would go out of bounds by height
        if to_y > wall_height:
            from_y -= wall_height
            to_y -= wall_height

        # TODO: make this actually replace something
        # actually replace the wall now
        mat[from_x:to_x][from_y:to_y] = wall

        return mat

class Matrix():
    width = None
    height = None
    matrix = None

    def __init__(self, width, height, matrix):
        self.width = width
        self.height = height
        self.matrix = matrix

    def __str__(self):
        return_str = ""
        if matrix:
            for x in matrix:
                for y in x:
                    if y < len(matrix[x]):
                        return_str = return_str + matrix[x][y]
                    else:
                        return_str = return_str + "\n"
            return return_str
        else:
            return ""

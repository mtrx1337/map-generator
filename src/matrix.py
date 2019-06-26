class Matrix():
    size = None
    matrix = None

    def __init__(self, size, matrix):
        self.size = size
        self.matrix = matrix

    def __str__(self):
        return_str = ""
        matrix = self.matrix
        if matrix:
            for x in matrix:
                for y in x:
                    return_str += str(x[y])
                return_str += "\n"
            return return_str
        else:
            return ""

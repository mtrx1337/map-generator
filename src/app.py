from flask import Flask, request
from matrixgen import Matrix_Gen
from serializer import Serialize

app = Flask(__name__)

"""
Generates a game matrix
"""
@app.route("/genmatrix")
def gen_matrix():
    mat_x_size = request.args.get('x')
    mat_y_size = request.args.get('y')
    # generate matrix
    matrix = Matrix_Gen.gen_matrix()
    # serialize it
    ser_matrix = Serialize.matrix(matrix)
    return ser_matrix

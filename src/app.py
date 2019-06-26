#!/bin/python3

from flask import Flask, request, Response, jsonify
from matrixgen import MatrixGen

app = Flask(__name__)

"""
Generates a game matrix and sends it to the client
"""
@app.route("/genmatrix")
def gen_matrix():
    error = None

    mat_x_size = request.args.get('x')
    mat_y_size = request.args.get('y')

    # generate matrix
    mg = MatrixGen()
    matrix = mg.gen_mat(mat_x_size, mat_y_size)
    if not matrix:
        error = {'error' : 'Error when generating matrix, generator returned `None`'}
        return jsonify(error)


    print(matrix.__str__())

    # print(json.dumps(matrix))

    return matrix.__str__()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

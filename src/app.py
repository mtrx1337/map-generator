#!/bin/python3

from flask import Flask, request, Response, jsonify
from matrixgen import MatrixGen
import json

app = Flask(__name__)

"""
Generates a game matrix and sends it to the client
"""
@app.route("/genmatrix")
def gen_matrix():
    error = None

    mat_size = int(request.args.get('size'))

    if not mat_size:
        error = {'error' : 'Faulty request, missing width argument'}
        return jsonify(error)

    if mat_size < 8:
        error = {'error' : 'Faulty request, matrix size has to be at least 8.'}
        return jsonify(error)

    # generate matrix
    mg = MatrixGen()
    mtrx = mg.gen_mat(mat_size)
    if not mtrx:
        error = {'error' : 'Error when generating matrix, generator returned `None`'}
        return jsonify(error)

    print(mtrx.__str__())

    return_json = {}
    return_json['size'] = mtrx.size
    return_json['matrix'] = mtrx.matrix

    return jsonify(return_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

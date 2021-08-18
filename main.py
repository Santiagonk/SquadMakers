from app.mathFunctions.mathFunctions import AddOne, CalculateMCM
from app.jokes.jokes import jokesRandom, jokesResponse, jokesSelect
from flask import Flask, jsonify


from app import create_app
from app.jokes import *
from app.mathFunctions import *

app = create_app()

@app.route("/", methods=['GET'])
def main():
    return "<p> Hello to my amazing Flask App </p>"


@app.route("/jokes", methods=['GET'])
@app.route("/jokes/", methods=['GET'])
def Jokes():
    url = jokesRandom()
    return jsonify({"message":jokesResponse(url)})


@app.route("/jokes/<name>", methods=['GET'])
def JokesId(name):
    url = jokesSelect(name)
    return jsonify({"message":jokesResponse(url)})


@app.route("/numbers/<numbers>", methods = ['GET'])
def mathEndpointList(numbers):
    mcm = CalculateMCM(numbers)
    return jsonify({"message":mcm})


@app.route("/number/<number>", methods = ['GET'])
def mathEndpoint(number):
    return jsonify({"message":AddOne(number)})
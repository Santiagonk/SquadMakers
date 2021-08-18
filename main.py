from app.jokes.jokes import jokesRandom, jokesResponse, jokesSelect
from flask import Flask, jsonify
import functools

from app import create_app
from app.jokes import *

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

@app.route("/math/<numbers>", methods = ['GET'])
def mathEndpointList(numbers):
    numbers = [int(i) for i in numbers.split(',')]
    numbersProof = [1]*len(numbers)
    numberNext = numbers
    loopProof = numbers == numbersProof
    mcmList = list()
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    count = 0
    while(not loopProof):
        numbers = [i/prime[count] if i%prime[count] == 0 else i for i in numbers]

        if numbers == numberNext:
            count += 1
        else:
            mcmList.append(prime[count])

        if numbers == numbersProof:
            loopProof = False
            break

        numberNext = numbers

        if count >= len(prime):
            break

    mcm = functools.reduce(lambda a, b: a*b, mcmList)


    return jsonify({"message":mcm})
from app.jokes.jokes import jokesRandom, jokesResponse, jokesSelect
from flask import Flask

from app import create_app
from app.jokes import *

app = create_app()

@app.route("/", methods=['GET'])
def main():
    return "<p> Hello to my amazing Flask App </p>"


@app.route("/jokes", methods=['GET'])
def Jokes():
    url = jokesRandom()
    return jokesResponse(url)


@app.route("/jokes/<name>", methods=['GET'])
def JokesId(name):
    url = jokesSelect(name)
    return jokesResponse(url)
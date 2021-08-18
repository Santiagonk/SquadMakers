from flask import Flask
from flask_restful import Resource, Api
import json
import requests
import random

from app import create_app

app = create_app()

@app.route("/", methods=['GET'])
def main():
    return "<p> Hello to my amazing Flask App </p>"


@app.route("/jokes", methods=['GET'])
def Jokes():
    dad_url = "https://icanhazdadjoke.com/slack"
    chuck_url = "https://api.chucknorris.io/jokes/random"
    url = random.choice([dad_url, chuck_url])
    r = requests.get(url)
    r = r.json()

    if url == dad_url:
        return r["attachments"][0]["text"]
    else:
        return r["value"]


@app.route("/jokes/<name>", methods=['GET'])
def JokesId(name):
    dad_url = "https://icanhazdadjoke.com/slack"
    chuck_url = "https://api.chucknorris.io/jokes/random"

    if name.lower() == "chuck":
        url = chuck_url
    elif name.lower() == "dad":
        url = dad_url
    else:
        raise ValueError

    r = requests.get(url)
    r = r.json()

    print(url)
    if url == dad_url:
        return r["attachments"][0]["text"]
    else:
        return r["value"]
from flask import Flask, Response, jsonify, Request, request
# import json
import wikipedia
import random

# import logging

app = Flask(__name__)


@app.route("/")
def homepage():
    return "<h1>Droplet runningggg</h1>"


@app.route("/request", methods=["POST"])
def query():
    data_raw = request.get_json()
    if data_raw:
        data = data_raw["find"]
        try:
            pgid = wikipedia.WikipediaPage(title=data).pageid
            out = wikipedia.WikipediaPage(pageid=pgid).summary
            link = wikipedia.WikipediaPage(pageid=pgid).url
            return jsonify(result=out, url=link)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            pgid = wikipedia.WikipediaPage(title=s).pageid
            out = wikipedia.WikipediaPage(pageid=pgid).summary
            link = wikipedia.WikipediaPage(pageid=pgid).url
            return jsonify(result=out, url=link)
        except wikipedia.PageError as p:
            return jsonify("No info available")
    else:
        return jsonify("Send data")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

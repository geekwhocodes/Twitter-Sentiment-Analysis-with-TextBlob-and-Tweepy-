import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)


import streamListener
import helper
import old_stats
import credentials
import old_stats


from tweepy import OAuthHandler 
from tweepy import Stream
import json

#Flask
from flask import Flask, render_template, json, jsonify

app = Flask(__name__)


def getStats():
    OldStats = old_stats.OldStats()
    return OldStats.getStats()

@app.route("/")
def main():
    return render_template('home.html')


@app.route("/stats")
def stats():
    return render_template('stats.html')


@app.route("/v1/stats")
def showStats():
    stats = getStats()
    return jsonify(results=stats)


if __name__ == "__main__":
    app.run()


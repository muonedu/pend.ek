#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template, redirect, request, url_for
from os import getenv
import random
import string

app = Flask(__name__)
port = int(getenv("PORT", 1212))

urls = {}

def get_url(shortedUrl):
    return urls.getvalue(shortedUrl)

def generate_id(url):
    return ''.join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(5))

def url_shortener(url):
    path = generate_id(url)
    urls[path] = url
    return "http://localhost:{}/{}".format(port, path)

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def main():
    if request.form['text']:
        shorted_url = url_shortener(request.form['text'])
        return render_template("index.html", data=shorted_url)
    else:
        return render_template('index.html')

@app.route("/<shortedUrl>")
def redirect_url(shortedUrl):
    if shortedUrl:
        url = urls.get(shortedUrl)
        if url:
            return redirect(url.encode('ascii'), 301)
        else:
            return redirect(url_for('index_page'), 301)    

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=port, threaded=True)

#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request 
from base64 import b64encode
from os import getenv

urls = {}
app = Flask(__name__)

port = int(getenv("PORT", 1212))

def GetUrl(shortedUrl):
    if shortedUrl:
        return urls.getvalue(shortedUrl)

def ShortenUrl(url):
    if url:
        port = str(getenv("PORT", 1212))
        urls[b64encode(url)] = url 
        return "http://localhost:{}/{}".format(port, b64encode(url))
    return False

@app.route("/")
def IndexPage():
    return render_template("index.html")

@app.route("/app", methods=["GET", "POST"])
def Main():
    url = request.form['text']
    if url:
        shortenurl = ShortenUrl(url)
        return render_template("app.html", data=shortenurl, url=url)

@app.route("/urls")
def ShowUrls():
    return render_template("urls.html", data=urls)

@app.route("/<shortedUrl>")
def Redirect(shortedUrl):
    if shortedUrl:
        url = urls.get(shortedUrl)  
        if url:
            return redirect(url.encode('ascii'), 301)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=int(getenv("PORT", 1212)), threaded=True
            )

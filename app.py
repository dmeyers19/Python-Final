# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: Destiny
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/first-year")
def Page_1():
    return render_template("page1.html")

@app.route("/summer-plans")
def Page_2():
    return render_template("page2.html")
#start the server
if __name__ == "__main__":
    app.run()
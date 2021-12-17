from flask import Flask 
import os 
import socket 

app = Flask(__name__)


@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hello")
def hello_test():
    html = "<h2> Hello From Docker & Python Flask Based Web App.!!</h2>"
    return html


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=8081)

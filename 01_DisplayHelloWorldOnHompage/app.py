## 1) import flask 
from flask import Flask

## 2) create flask app
app = Flask(__name__)

## 3) write function
@app.route('/')
def hello():
    return "Hello World!"

## 4) write standard protocol to trigger the flask application
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
## 1) import flask
from flask import Flask , request

## 2) create flask app
app = Flask(__name__)

## 3) write the function
@app.route('/')
def homepage():
    return "Welcome to the Home Page.\nPass your name to the userinfo function through the url parameter to display it on to the page."

@app.route('/userinfo')
def displayInfo():
    name = request.args.get('name')
    return f"Your name is : {name}!"


## 4) Trigger the flask app by writing standard protocol
if __name__ == '__main__':
    app.run(host='0.0.0.0')
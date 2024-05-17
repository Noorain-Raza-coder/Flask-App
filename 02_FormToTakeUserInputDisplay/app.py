## 1) import flask
from flask import Flask , render_template , request

## 2) create flask app
app = Flask(__name__)

## 3) write the function
@app.route('/')
def formPage():
    return render_template('index.html')

@app.route('/displayInfo', methods = ['POST'])
def displayInfo():
    userName = request.form.get('userName')
    userAge = request.form.get('userAge')
    userGender = request.form.get('userGender')

    return f"User Name : {userName} , User Age : {userAge} , User Gender : {userGender} "


## 4) write standard protocol to triger the flask app
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
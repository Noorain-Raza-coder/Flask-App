## 1) import library
from flask import Flask , render_template

## 2) create flask app
app = Flask(__name__)

## 3) write function
@app.route('/' , methods = ['POST'])
def homepage():
    return render_template('home.html')

@app.route('/secondpage', methods = ['POST'])
def page2():
    return render_template('page2.html')

## 4) trigger it by writing standard protocol
if __name__ == '__main__':
    app.run(host='0.0.0.0')
# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/level1')
def level1():
    return render_template("level1.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
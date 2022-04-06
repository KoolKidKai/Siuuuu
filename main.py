# import "packages" from flask
from flask import Flask, render_template
from __init__ import app

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api


app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/level1/')
def level1():
    return render_template("level1.html")

@app.route('/level2/')
def level2():
    return render_template("level2.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
from flask import render_template
from __init__ import app


from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/level1')
def level1():
    return render_template("level1.html")

@app.route('/level2')
def level2():
    return render_template("level2.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")
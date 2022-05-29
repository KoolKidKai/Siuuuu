from flask import render_template, redirect, url_for, request, send_from_directory
from __init__ import app, login_manager
from flask_login import login_required

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from cruddy.app_notes import app_notes

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    app.config['NEXT_PAGE'] = request.endpoint
    return redirect(url_for('login'))
# Route for handling the login page logic


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'SIUUU' or request.form['password'] != 'coding':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('index.html')
    return render_template('login.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




@app.route('/notes')
def notes():
    return render_template("notes.html")
#@app.errorhandler(404)
#def page_not_found(e):
#    # note that we set the 404 status explicitly
#    return render_template('404.html'), 404



@app.route('/calendar2')
def calendar2():
    return render_template("calendar2.html")

@app.route('/clubRoster')
def clubRoster():
    return render_template("clubRoster.html")

@app.route('/join')
def join():
    return render_template("join.html")



if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")
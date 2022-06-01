from flask import render_template, redirect, url_for, request, send_from_directory
from __init__ import app
from datetime import datetime
import calendar
from flask_login import login_required

from cruddy.app_crud import app_crud
from uploady.app_upload import app_upload
from cruddy.app_crud_api import app_crud_api
from notey.app_notes import app_notes

app.register_blueprint(app_upload)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)





@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'SIUUU' or request.form['password'] != 'coding':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('index.html')
    return render_template('login.html', error=error)


@app.route('/uploads/<name>')
def uploads_endpoint(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# register "uploads_endpoint" endpoint so url_for will find all uploaded files
app.add_url_rule(
    "/volumes/uploads" + "/<name>", endpoint="uploads_endpoint", build_only=True
)


@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




@app.route('/hackclub_notes_upload')
def none():
    return render_template("notes.html")
#@app.errorhandler(404)
#def page_not_found(e):
#    # note that we set the 404 status explicitly
#    return render_template('404.html'), 404

@app.route('/calendar')
def cal():
    currentday = datetime.now().day
    monthnum = datetime.now().month
    currentmonth = calendar.month_name
    currentyear = datetime.now().year
    return render_template("calendar.html", currentday=currentday, monthnum=monthnum, currentmonth=currentmonth, currentyear=currentyear)



@app.route('/calendar2')
def calendar2():
    return render_template("calendar2.html")

@app.route('/clubRoster')
def clubRoster():
    return render_template("clubRoster.html")

@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/tasklist')
def tasklist():
    return render_template("tasklist.html")



if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")
from flask import render_template, url_for, flash
from app import app, db
#from app.form import LoginForm
#need to build forms
from werkzeug.urls import url_parse
#from app.medels import User
#need to build User

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    pass

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        #need form shell_context_processo
    pass

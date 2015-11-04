import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Guest'}  # fake user
        return render_template('index.html',
                           title='Home',
                           user=user)

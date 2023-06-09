# Old version of main file kept for posterity
import requests, json
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from datetime import date

app = Flask(__name__)
bootstrap = Bootstrap5(app)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

thism = 5
thisd = 4
endpoint = endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{thism}/{thisd}"


@app.route('/', methods=('GET', 'POST'))
def main():
    m = 13
    setdate = date(2023, thism, thisd)
    printdate = f"{setdate.strftime('%B')} {thisd}"
    try:
        r = requests.get(endpoint)
        data = r.json()
    except:
        print('please try again')
    return render_template('index.html', data=data, m=m, d=printdate)
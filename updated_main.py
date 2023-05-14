import requests
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

today = datetime.now()
thism = today.month
thisd = today.day
endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{thism}/{thisd}"

@app.route('/', methods=('GET', 'POST'))
def main():
    global thism, thisd, endpoint

    if request.method == 'POST':
        selected_date = request.form['date-pick']
        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
            thism = selected_date.month
            thisd = selected_date.day
            endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{thism}/{thisd}"
            r = requests.get(endpoint)
            data = r.json()
            return render_template('index.html', data=data, m=0, d=selected_date.strftime('%B %d'))
        except ValueError:
            return redirect('/')
    else:
        setdate = datetime(2023, thism, thisd)
        printdate = f"{setdate.strftime('%B')} {thisd}"
        try:
            r = requests.get(endpoint)
            data = r.json()
        except:
            print('please try again')
        return render_template('index.html', data=data, m=13, d=printdate)

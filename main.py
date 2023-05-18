import requests
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#setting the user imput as a varible.
today = datetime.now()
thism = today.month
thisd = today.day
#Website API with user inputs
endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{thism}/{thisd}"
item = 0
l = ""
z = 0


@app.route('/', methods=('GET', 'POST'))
def main():
    global thism, thisd, endpoint, item, l, z
    #when correct format of date is entered the program contiunes to the try statement  and executes.
    if request.method == 'POST' and 'date-pick' in request.form:
        selected_date = request.form['date-pick']
        try:
            #Date entered is saved as selected_Date
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
            #today.month, user selected month
            thism = selected_date.month
              #today.day, user selected day
            thisd = selected_date.day
            l = f"{selected_date.strftime('%B')} {thisd}"
            #Adds date into API
            endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{thism}/{thisd}"
            r = requests.get(endpoint)
            data = r.json()
            item = 0
            #Length of api within seached field tp display correct total value.
            z = len(data["events"])
            return render_template('index.html', data=data, m=item, d=f"{selected_date.strftime('%B')} {thisd}")
        except ValueError:
            #if not vaild date the program will default back to / directory
            return redirect('/')
    elif request.method == 'POST' and 'shift' in request.form:
        try:
            r = requests.get(endpoint)
            data = r.json()
        except:
            print('please try again')

        if request.form['shift'] == 'back':
            # when back  arrow is pressed the item value varible is subtracted by 1 and then the program is ran again
            if item > 0:
                item = item - 1
                return render_template('index.html', data=data, m=item, d=l)
            else:
                #Reroute to home directory
                return redirect("/")
        elif request.form['shift'] == 'next':
            # when forward  arrow is pressed the item value varible is subtracted by 1 and then the program is ran again
            if item < z:
                item = item + 1
                return render_template('index.html', data=data, m=item, d=l)
            else:
                      #Reroute to home directory
                return redirect("/")
    else:
        setdate = datetime(2023, thism, thisd)
        printdate = f"{setdate.strftime('%B')} {thisd}"
        l = printdate
        try:
            r = requests.get(endpoint)
            data = r.json()
            z = len(data["events"])
        except:
            print('please try again')
        return render_template('index.html', data=data, m=item, d=l)

from flask import Flask, render_template, request
import requests
import pandas as pd
import numpy as np


my_excel = pd.read_csv('data.csv')

my_dict = my_excel.to_numpy()

ppc = 0

app = Flask(__name__)


@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/')
def home1():
    return render_template('index.html')
@app.route('/booked')
def book():
    return render_template('book.html')

@app.route('/covid19')
def covid():
    return render_template('covid.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/destination',methods =["GET", "POST"])
def plans():
    if request.method == "POST":
        forminput = request.form
        fromplanet = forminput['from']
        toplanet = forminput['to']
        option = forminput['option']
        no_passengers = forminput['passengers']

        for i in range(len(my_dict)):
            if fromplanet == my_dict[i][0] and toplanet == my_dict[i][1] and option == my_dict[i][2]:
                ppc = my_dict[i][3]
                fin_ppc = ppc*int(no_passengers)
                ppc = {"ppc":ppc}
                fin_ppc1 = {"fin_ppc":fin_ppc}
                nopassengers = {"pass":no_passengers}
                to = {"dest":toplanet}
                from1 = {"fr":fromplanet}
                classs = {"cl":option}
                
                if toplanet == "Mercury":
                    return render_template("mercury.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Venus":
                    return render_template("venus.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Earth":
                    return render_template("earth.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Mars":
                    return render_template("mars.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Jupiter":
                    return render_template("jupiter.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Saturn":
                    return render_template("saturn.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Uranus":
                    return render_template("uranus.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
                elif toplanet == "Neptune":
                    return render_template("neptune.html",**ppc,**fin_ppc1,**nopassengers,**to,**from1,**classs)
    return render_template('destination.html')

@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == "POST":
        forminput = request.form
        email = forminput['email']
        print(email)
        thankyou = {"thank":"Our Customer Care Executive will reach you soon."}
        return render_template("support.html", **thankyou)
    return render_template('support.html')

if __name__ == "__main__":
    app.run(debug = True)

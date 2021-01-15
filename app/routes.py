from flask import Flask, render_template, request
from app.static.scripts.script import run_script
from app import app

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results(dayName, akanName):



    return render_template('results.html', dayName=dayName, akanName=akanName)


#!C:\Users\alokk\AppData\Local\Programs\Python\Python311
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	#Location of html file are always inside templates folder

@app.route('/data/')
def data():
	return render_template('data.html')


app.run('localhost', 80)


'''
Jade Pearl
SDEV 300 Lab 6
This Lab consists of Python Flask which routes to a simple webpage made using HTML and CSS.
My webpage is a Fan-made Lord of the Rings Website
'''
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    '''
    Routes to the home page
    '''
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('home.html', current_datetime=current_datetime)

@app.route('/fotr')
def fotr():
    '''
    Routes to the page for Fellowship of the Ring
    '''
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('fotr.html', current_datetime=current_datetime)

@app.route('/ttt')
def ttt():
    '''
    Routes to the page for The Two Towers
    '''
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('ttt.html', current_datetime=current_datetime)

@app.route('/rotk')
def rotk():
    '''
    Routes to the Return of the King
    '''
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('rotk.html', current_datetime=current_datetime)

if __name__ == '__main__':
    app.run(debug=True)

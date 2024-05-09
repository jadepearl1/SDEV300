from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return show_hello()

# Can call functions as part of the returns
def show_hello():
 return 'Hello, UMGC SDEV Students!'

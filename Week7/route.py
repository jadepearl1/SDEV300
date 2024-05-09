'''
Jade Pearl
SDEV 300 Lab 6
This Lab consists of Python Flask which routes to a simple webpage made using HTML and CSS.
My webpage is a Fan-made Lord of the Rings Website
'''
from datetime import datetime
import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import sha256_crypt

app = Flask(__name__)

app.secret_key = secrets.token_hex(12)

def password_complexity(password):
    '''
    Checks a password for proper complexity
    '''
    return (
        len(password) >= 12
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password)
    )

def write_to_file(username, hashed_pass):
    '''
    Writes a new user registration to a file called passfile
    '''
    with open('passfile', "a", encoding="utf-8") as file:
        file.write(f"{username}:{hashed_pass}\n")

def user_exists(username):
    '''
    Checks if a user already exists in the passfile file. This also helps with login
    '''
    with open('passfile', "r", encoding="utf-8") as file:
        lines = file.readlines()
        return any(username in line for line in lines)

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
    Routes to the page for Fellowship of the Ring upon successful login
    '''
    if 'username' not in session:
        return redirect(url_for('login'))

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('fotr.html', current_datetime=current_datetime)

@app.route('/ttt')
def ttt():
    '''
    Routes to the page for The Two Towers upon successful login
    '''
    if 'username' not in session:
        return redirect(url_for('login'))

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('ttt.html', current_datetime=current_datetime)

@app.route('/rotk')
def rotk():
    '''
    Routes to the Return of the King upon successful login
    '''
    if 'username' not in session:
        return redirect(url_for('login'))

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('rotk.html', current_datetime=current_datetime)

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Routes to the user registration form and checks if the user entered already exists and if the
    password meets complexity requirements. If the user does not exist already, it will be written
    to passfile. Has new users login after registration
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_exists(username):
            return render_template('register.html', message='Username already exists. Choose a \
            different one.')

        if not password_complexity(password):
            return render_template('register.html', message='Password does not meet complexity \
            requirements. Have at least 12 characters containing at least one uppercase letter \
            , one lowercase letter, one number, and one special character.')

        hashed_password = sha256_crypt.hash(password)
        write_to_file(username, hashed_password)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Routes to the user login page. The user's name and password are verfied.
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('passfile', 'r', encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and sha256_crypt.verify(password, stored_password):
                session['username'] = username
                return render_template('loggedin.html', username=username)

        return render_template('login.html', message='Invalid username or password. Username or \
        password may not exist or may be incorrect.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    '''
    Redirects to the home page when a user logs out of the website. The session with that user ends.
    '''
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

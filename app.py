from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'your secret key'


# correct database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'year_task'
app.config['MYSQL_PORT'] = 3307

# Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account WHERE first_name = %s AND pass = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['first_name']
            session['user_id'] = account['id']
            msg = 'Logged in successfully!'
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and \
            'username' in request.form and 'password' in request.form and 'phone_number' in request.form and \
            'address' in request.form and 'email' in request.form:
        first_name = request.form['username']
        last_name = request.form['last_name']
        password = request.form['password']
        phone_number = request.form['phone_number']
        address = request.form['address']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO account (first_name, last_name, pass, phonenr, adress, mail) VALUES (%s, %s, %s, %s, %s, %s)',
                       (first_name, last_name, password, phone_number, address, email))
        mysql.connection.commit()
        msg = 'You have successfully signed up!'
        return redirect(url_for('login'))
    return render_template('signup.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))


##I'm sorry young me

# @app.route('/add_values', methods=['GET', 'POST'])
# def add_values():
#     msg = ''
#     if request.method == 'POST' and 'nok' in request.form and 'interest' in request.form:
#         nok = request.form['nok']
#         interest = request.form['interest']
#         name = request.form['name']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         user_id = session['user_id']
#         cursor.execute('INSERT INTO konto (nok, interest, user_id, konto_name) VALUES (%s, %s, %s, %s)', (nok, interest, user_id, name))
#         mysql.connection.commit()
#         msg = 'Values added successfully!'
#     return render_template('add_values.html', msg=msg)



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'your secret key'

app.static_folder = 'static'


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
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/browse')
def browse():
    if 'loggedin' in session:
        game_id=[]
        game_name=[]
        game_desc=[]
        game_img=[]
        gameamount=[]
        looped=0
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM game WHERE game_id=(SELECT max(game_id) FROM game);")
        gameidget = cursor.fetchone()
        game_ids = gameidget['game_id']
        
        # cursor.execute('SELECT * FROM game WHERE game_name = %s', (game_name))
        for i in range(1, game_ids+1):
            cursor.execute(f"SELECT * FROM game WHERE game_id = '{i}'")
            game = cursor.fetchone()
            game_id.append(game['game_name'])
            game_name.append(game['game_name'])
            game_desc.append(game['game_desc'])
            game_img.append(game['game_img'])
            gameamount.append(looped)
            looped+=1

        # content = f"<section id='egggame' class='gamesection'> <h3>Survival egg</h3> <p>{ game_name[0] }</p> <div class='img_txt'> <img src='static/img/{game_img[0]}' alt='egg jumping'> <p>{game_desc[0]}</p> </div> <button>add to library</button> </section>"
        # if request.method=='POST':
            


    return render_template('browse.html', username=session['username'],gname=game_name,gdesc=game_desc,gimg=game_img,glen=gameamount, gid=game_id)
    # return redirect(url_for('login'))


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

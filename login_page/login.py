import mysql.connector
from flask import (Flask, request, redirect, render_template, session)

app = Flask(__name__)
app.secret_key = 'secretkey'

conn = mysql.connector.connect(
  host="localhost", 
  user="root", 
  password="",
  database="exp"
  )
cursor = conn.cursor()
# cursor.execute("CREATE DATABASE exp")
query = ("CREATE TABLE user2(id int PRIMARY KEY,username varchar(255) NOT NULL,password varchar(255) NOT NULL)")
cursor.execute(query)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()
    if user:
      session['username'] = username
      return redirect('/')
    else:
      error = 'Incorrect username or password'
      return render_template('index.html', error=error)
  return redirect('/')

if __name__ == '_main_':
  app.run(debug=True)
import mysql.connector

conn = mysql.connector.connect(
  host="localhost", 
  user="root", 
  password="",
  database="exp"
  )
cursor = conn.cursor()
# cursor.execute("CREATE DATABASE exp")
query = ("CREATE TABLE user1(username varchar(255) NOT NULL,password varchar(255) NOT NULL)")
cursor.execute(query)
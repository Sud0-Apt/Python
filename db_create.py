import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "skanda"                     #use of db name after creation
)

objp = db.cursor()

# objp.execute("CREATE DATABASE skanda")    #CREATING A DATABASE 

student = ("CREATE TABLE STUDENT(USN INT,NAME VARCHAR(25),GENDER VARCHAR(10))")
# query = "Drop table STUDENT;"
objp.execute(student)
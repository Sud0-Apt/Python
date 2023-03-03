import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "college",
)


myobj = db.cursor()

# student = ("create table student(usn int,name varchar(25))")
# dept = ("create table dept(d_id int,d_name varchar(25))")

# myobj.execute(student)
# myobj.execute(dept)

sql = "INSERT INTO student (usn, name) VALUES (%s, %s)"
val = ("1", "CSE")
   
myobj.execute(sql, val)
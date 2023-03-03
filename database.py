import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "employee"
)

obj = db.cursor()

a = ("CREATE TABLE emp1(id int,name varchar(25),age int)")

obj.execute(a)

# query = "INSERT INTO emp(id,name,age) VALUES (%s,%s,%s)"
# val = ("1","skanda","19")

# obj.execute(query,val)

db.commit()
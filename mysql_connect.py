# importing required libraries
import mysql.connector

db = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
database = "pytproject"
)

print(db)

# Disconnecting from the server
db.close()
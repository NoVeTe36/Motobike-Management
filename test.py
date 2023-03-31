import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = "tungntl1234",
    database = "motorbikemanagement",
)

cursor = db.cursor()
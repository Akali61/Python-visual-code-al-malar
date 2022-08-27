import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "A20022006Kt@S",
    database = "node-app"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
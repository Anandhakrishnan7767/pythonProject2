import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="Kannan@1999"
)
db=mydb.cursor()
# print(db)

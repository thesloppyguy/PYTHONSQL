import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)

print(mydb)
# <mysql.connector.connection.MySQLConnection object at 0x000001FCEE181F70>

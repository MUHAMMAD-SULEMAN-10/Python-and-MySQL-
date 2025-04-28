#databese connectivity 
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database = 'db1'
 )

if conn.is_connected():
    print("connection is established...")
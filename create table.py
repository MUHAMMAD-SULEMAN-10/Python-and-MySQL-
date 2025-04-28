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

# Create Database:


#conn is our variable which has connection store.
# cursor is a function we are calling it and obtian the cursor object and cursor oject has execute funtion to perfrom quries.
# cur=conn.cursor()
# cur.execute("CREATE DATABASE db1")


#create table:
# cur=conn.cursor()
# s = "CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
# cur.execute(s)

#Another way to create a table in a particluar database:
cur=conn.cursor()
cur.execute('create table db1.fsds(studentid int , firstname varchar(50) , lastname varchar(50) , registration DATE , class varchar(20) , course_name varchar(5))')


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

#insertdata/records in the particular database/table of columns
cur=conn.cursor()
cur.execute("insert into db1.fsds values(123 , 'Muhammad', 'Suleman', '2022-11-11', 'sql', 'fsds')")

conn.commit()
#this is going to return me some sorts of results
cur.execute('select * from db1.fsds')

# for i in cur:
#     print(i) 
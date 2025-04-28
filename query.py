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

cur=conn.cursor()

#query select all the table coloumns
cur.execute("select * from db1.fsds")
for  i in cur:
    print(i)

#query select specific columns names
cur.execute('select studentid, firstname, class from db1.fsds')
for i in cur:
    print(i)


#Multiple sql commands:

#give me only those records where id is only 130
#we use where clause
cur.execute('select * from db1.fsds where studentid = 130')
for i in cur:
    print(i)

#query fetech record where student id is greate > than  130 
cur.execute('select * from db1.fsds where studentid > 130')
for i in cur:
    print(i)

#query based on and condition or conditions 
cur.execute("select * from db1.fsds where firstname = 'Muhammad' and class = 'sql' ")
for i in cur:
    print(i)

#query we have an id 125 and changed its firstname 
#we need to used the update command for it.

#Note: when do update , insert, delete commands then we need to commit first 

cur.execute("update db1.fsds set firstname = 'Afzal' where studentid = 124 ")
conn.commit()

#query update the class name sql to mysql 
cur.execute(" update db1.fsds set class = 'mysql' ")
conn.commit()

#Delete the record of where name is Ashraf
cur.execute("delete from db1.fsds where lastname = 'Ashraf' ")
conn.commit()


#Query fetech the very first student id from the record/minimum id same as max id/last id 
#here we used the min function 
cur.execute("select min(studentid) from db1.fsds ")
for i in cur:
    print(i)


#query fetch total number of records inside the databases 
cur.execute('select count(*) from db1.fsds')
for i in cur:
    print(i)

#UPDATE the class name and record of studentid between 125 and 128 
cur.execute("update db1.fsds set class = 'sql' where studentid between 125 and 128")
conn.commit()
#UPDATE the class name and record of studentidbetween 129 and 132
cur.execute("update db1.fsds set class = 'MongoDB' where studentid between 129 and 132")
conn.commit()


#query to fecth all It groups all rows by class.
#Then counts the number of rows in each group (class).
cur.execute("select count(*) from db1.fsds group by class")
for i in cur:
    print(i)

#query to fecth all It groups all rows by class with names and how many times names is repeated also give.
#Then counts the number of rows and names in each group (class).
cur.execute("select count(*),class from db1.fsds group by class")
for i in cur:
    print(i)

#DROP table command
# cur.execute("drop table db1.fsds")
# conn.commit()

#query drop the databese
# cur.execute("drop database db1")




#Always close the connection
cur.close()
conn.close()
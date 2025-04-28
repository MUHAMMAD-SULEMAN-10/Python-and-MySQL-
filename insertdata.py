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
cur.execute("""insert into db1.fsds values(123 , 'Muhammad', 'Suleman', '2022-11-11', 'sql', 'fsds'),
(122 , 'Muhammad', 'Usman', '2022-11-25', 'MY_SQL', 'fsds'),
(124 , 'Ali', 'Khan', '2022-11-12', 'Python', 'fsds'),
(125 , 'Usman', 'Ashraf', '2022-11-13', 'Data Science', 'fsds'),
(126 , 'Fatima', 'Noor', '2022-11-14', 'Machine Learning', 'fsds'),
(127 , 'Ahmed', 'Raza', '2022-11-15', 'Deep Learning', 'fsds'),
(128 , 'Ayesha', 'Siddiqui', '2022-11-16', 'AI', 'fsds'),
(129 , 'Bilal', 'Qureshi', '2022-11-17', 'Big Data', 'fsds'),
(130 , 'Hassan', 'Javed', '2022-11-18', 'Cloud Computing', 'fsds'),
(131 , 'Zainab', 'Iqbal', '2022-11-19', 'Blockchain', 'fsds'),
(132 , 'Saad', 'Malik', '2022-11-20', 'Cyber Security', 'fsds')
""")

conn.commit()
#this is going to return me some sorts of results
cur.execute('select * from db1.fsds')

for i in cur:
    print(i) 
import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test-shiro')
cursor = conn.cursor()
cursor.execute('select * from user ')
values = cursor.fetchall()
for value in values:
    print(value)
cursor.close()
conn.close

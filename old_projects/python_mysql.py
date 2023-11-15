# Tested and worked 10/12/23 - Must enter password again for each query; do not share! Personal Info!

import mysql.connector

config = {"host": "localhost", "user": "root", "password": "", "database": "Oracle_HR"}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
select_query = "SELECT * FROM emp"

cursor.execute(select_query)
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()

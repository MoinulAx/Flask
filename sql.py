import pymysql.cursors
import pymysql

connection= pymysql.connect(
   
    host="10.100.33.60",
    user="mkhan",
    password='221085624',
    database='world',
    cursorclass=pymysql.cursors.DictCursor

)

cursor= connection.cursor()

cursor.execute("SELECT * FROM `country`")

result= cursor.fetchall()

print(result)

print(type(result))

print(result[3]['HeadofState'])
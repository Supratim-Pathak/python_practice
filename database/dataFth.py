import mysql.connector
from mysql.connector import errorcode

conn = {
    'host':'localhost',
    'username':'root',
    'password':'',
    'database':'delight1_delightedfamilyindia'
}

try:
    connect = mysql.connector.connect(**conn)
    query = ("SELECT * FROM `about_us`")
    cursor = connect.cursor()
    cursor.execute(query)
    data  = cursor.fetchall()
    print(data)
except mysql.connector.Error as e:
    print(e.msg)  
finally:
    connect.close()
import mysql.connector
from mysql.connector import errorcode
conn = {
    'host':'localhost',
    'database':'delight1_delightedfamilyindia',
    'user' : 'root',
    'password':''    
}
try:
    connection = mysql.connector.connect(**conn)
    query = ("SELECT * FROM `user`")
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    for i in record:
        myfile = open("database.txt","a+")
        myfile.write(str(i))
    myfile.close()   

except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)

cursor.close()

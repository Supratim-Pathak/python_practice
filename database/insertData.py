import mysql.connector
try:
    coConfig = {
        'host' : 'localhost',
        'username' : 'root',
        'password' : '',
        'database' : 'test'
    }
    conn = mysql.connector.connect(**coConfig)
    if conn.is_connected():
        print('connected')     
except mysql.connector.Error as err:
    print(err.msg)

# TAKING USER INPUT

Username = input("Enter username:")
Password = input("Enter Password:")

sql = "INSERT INTO `superuser`(`username`, `password`) VALUES (%s,%s)"
val = (Username, Password)
cursor = conn.cursor()
try:
    cursor.execute(sql, val)
    conn.commit()
    print('Data Inserted !!!',cursor.rowcount)
except mysql.connector.Error as err:
    conn.rollback()
    print('Some Error Occured !!!', err.msg)

conn.close()
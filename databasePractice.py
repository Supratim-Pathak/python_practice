import mysql.connector

connConmfig ={
    'host' : 'localhost',
    'username' : 'root',
    'password' : '',
    'database' : 'delivery_dits',
}

try:
    conn = mysql.connector.connect(**connConmfig)
    query = ("SELECT * FROM `account_master`")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    for i in range(0, len(result), 1):
        for j in range(0, len(result[i])):
            print(result[i][j])
            
except mysql.connector.Error as err:
    print(err.msg)
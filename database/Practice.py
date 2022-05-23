import mysql.connector 
conn = {
    'host' : 'localhost',
    'username' : 'root',
    'password' : '',
    'database' : 'ajaxcrud',
}
con = mysql.connector.connect(**conn)

try:
    if(con.is_connected()):
        cursor = con.cursor()
        sql = "INSERT INTO `emp`(`name`, `skills`, `address`, `designation`, `age`, `country`) VALUES (%s,%s,%s,%s,%s,%s)"
        params = ('Supratim','Python','Barasat','Developer', 27,'India')
        cursor.execute(sql, params)
        con.commit()
except mysql.connector.Error as err :
    con.rollback();
    print(err.msg)



import mysql.connector
from mysqlx import Column
from numpy import append
import pandas as pd

config = {
    'host' : 'localhost',
    'username' : 'root',
    'password' : '',
    'database' : 'ajaxcrud',
}
conn = mysql.connector.connect(**config)

data = pd.read_csv('data_csv.csv')
mydata = []
# for i in data:
#     mydata.append(i)

print(mydata)
print(data)
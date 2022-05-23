import pandas as pd

# data = read_csv('Admin Panel.csv')
# print(data)

# json_data = pd.read_json('ProductJson.json')
# print(json_data.head())

data = pd.read_excel('Admin Panel.xlsx', header=None)
f_one = open('excelBulkData.txt', 'a+')
f_one.write(str(data))
f_one.close()
print(data)





import pandas

df1 = pandas.DataFrame([[4,3,2,7],
                        [1,12,32,24],
                        [10,24,4,455],
                        ],
                    columns=['a','b','c','d']
                        )
df1.to_excel('E:/myDataFrame.xlsx', sheet_name='Sheet1')
print(df1)
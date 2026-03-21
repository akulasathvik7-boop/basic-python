# import pandas as pd
# import numpy as np

#------------------------------------------------------------------------------------------
 #working with list

# data=[1,2,3,4]
# raw_data=pd.Series(data,index=['p1','p2','p3','p4'])
# print(raw_data)
# print(raw_data.loc['p1'])
# print(raw_data.iloc[2])

# change=raw_data.loc['p1']*10
# print(change)
# print(raw_data*10)

# raw_data.loc['p2']=27
# print(raw_data.loc['p2'])

# raw_data.iloc[0]=6
# print(raw_data.loc['p1'])

# print(raw_data[raw_data>=3])
# print(raw_data[raw_data%2==0])


#--------------------------------------------------------------------------------------

#working with dictinoaries

# rate_of_books={'the warrior':3000,'rising sun':5000,'captian':2900,'brother will':4000}
# order=pd.Series(rate_of_books)
# print(order)
# print(order.loc['the warrior'])
# print(order.iloc[3])


#--------------------------------------------------------------------------------------

#dataframes

# data={'name':['john','michael','sarah','lisa'],'age':[25,30,22,28],'city':['new york','los angeles','chicago','houston']}

# df=pd.DataFrame(data,index=[1,2,3,4])
# print(df)
# print(df.loc[1])
# print(df.loc[2])
# print(df.loc[3])
# print(df.loc[4])

# df.loc[1]={'name':"sathvik",'age':24,'city':"mahabubabad"}

# df.loc[2]={'name':"tharun",'age':23,'city':"mahabubabad"}

# df.loc[3]={'name':"prem",'age':25,'city':"mahabubabad"}

# df.loc[4]={'name':"laxman",'age':23,'city':"mahabubabad"}
# print(df)

# for i in range(0,4):
#     print(df.iloc[i])

##### add the column

# df['job']=['software','hardware','civil','dataScience']

# for i in range(0,4):
#     print(df.iloc[i])

# print(df['age'])


#### add rows

# new_row=pd.DataFrame([{'name':"sandy",'age':21,'city':'mhbd','job':'editor'},{'name':"sanjay",'age':22,'city':'warangal','job':'designer'}
#                       ]
#                      ,index=[5,6])
# df=pd.concat([df,new_row])
# print(df)
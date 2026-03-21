import pandas as pd
import numpy as np


data=[1,2,3,4]
raw_data=pd.Series(data,index=['p1','p2','p3','p4'])
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
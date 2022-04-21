from pickle import FALSE
import pandas as pd

"""
SERIES
A one-dimensional labeled array capable of holding any data type
"""

s = pd.Series([3, -5, 7, 4], index=['a', False, 'c', .34])
print(s)



print("...........................................")
'''
DataFrame

A two-dimensional labeled data structure with columns of potentially
different types
'''
data = {

    'Country': ['Belgium', 'India', 'Ghana', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Accra', 'Brasilia'],
    'Population':[145000000, 1300000000, 31000000, 207000000]

}

data_frame = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

print(data_frame)
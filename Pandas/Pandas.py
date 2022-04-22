import pandas as pd

"""
SERIES
A one-dimensional labeled array capable of holding any data type
"""

S = pd.Series([3, -5, 7, 4], index=['a', False, 'c', .34])

print(S)


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


na = ['Elijah', 'Elisha', 'Mary', 'Emma', 'David']
addr = ['London, UK', 'Canada', 'China', 'Germany, Hamburg', 'USA']
cont = [+44555332384, +12300444833, +86747282993, +46729882939, +12283489304]
occup = ["Software Engineer", "Executive Director",
         "Medical Practitioner", "Senior Engineer", "Engineer Manager"]
cmpny = ["Bloomberg", "Pure-Gold, Ca",
         "Huoung Medical Center", "Amazon", "Newmont Ltd."]

dic = {
    "NAME": na,
    "ADDRESS": addr,
    "CONTACT": cont,
    "COMPANY": cmpny,
    "OCCUPATION": occup
}

newDic = pd.DataFrame(dic)
print(newDic)
print("...........................................")

row_labels = ['ONE', 'TWO', 'THREE', 'FOUR']

data_frame = pd.DataFrame(data)

print(data_frame)
print("...........................................")

data_frame.index = row_labels
print(data_frame)

print("...........................................")

print(data_frame.iloc[0], ) # prints the second column of the table


print("...........................................")
# help(pd.concat)

f = data_frame.drop("Country", axis=1)

print(f)
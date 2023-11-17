# set1={'Fender','Gibson','Marshall','Ibanez'}
# set2={'Fender','Peavey','Boss'}
# set3={'Fender','Boss','Peavey'}

# print('cheacking ifor set content equality: ',set2==set3)
# print('checking for reference eequality: ',set2 is set3)
# print(id(set2),id(set3))

# print('unique elements from both sets: ',set1.intersection(set2))
# print('unique elements from both sets assigned to the first on: ',set1.intersection_update(set1) )

# print('unique elements in the first set: ',set1.difference(set2))

# print('Elements that are not shared by both sets are: ',set1.symmetric_difference(set2))

# print('')

# mystring='This is an example and we want to kno the length of this example!'
# lsit1=[1,2,3,4,5,'6','7',False]
#print(len(lsit1))
# for x in range(len(mystring)):
#     print('items number: '+ str(x+1)+' item name: ' + str(mystring[x]))
# counter=0
# for i in mystring:
#     print(f'item number: {counter}, Item value: {i}.')
#     counter+=1

# myDict={'key1':'1','key2':'2','key3':'3'}
# for x in myDict:
#     print(x[:])

# mySet={'value1','value2','value3','value4','value5','value6','value7'}
# for x,y in enumerate (mySet):
#     print(x,y)

# list1= ['string','another',True,False,1,3,5]
# list2=[1,2,3,4,5,6,7]
# list3=zip(list1,list2)
# print(list3)
# for x in list3:
#     print(x)

# from pprint import pprint


# books = {
#   'Harry Potter And The Sorcerers Stone': 1241100000,
#   'Harry Potter And The Chamber Of Secrets': 771300000,
#   'Harry Potter And The Prisoner Of Azkaban': 65210000,
#   'Harry Potter And The Goblet Of Fire': 645600000,
#   'Harry Potter And The Order Of The Phoenix': 635600000,
#   'Harry Potter And The Half Blood Prince': 661300000,
#   'Harry Potter And The Deathly Hallows ': 652200000,
# }
# sales = []
# book = []

# for key,value in books.items():
#     sales.append(value)
#     book.append(key)

# from pprint import pprint


# books = {
#   'Harry Potter And The Sorcerers Stone': 1241100000,
#   'Harry Potter And The Chamber Of Secrets': 771300000,
#   'Harry Potter And The Prisoner Of Azkaban': 65210000,
#   'Harry Potter And The Goblet Of Fire': 645600000,
#   'Harry Potter And The Order Of The Phoenix': 635600000,
#   'Harry Potter And The Half Blood Prince': 661300000,
#   'Harry Potter And The Deathly Hallows ': 652200000,
# }
# sales = []
# book = []

# for key,value in books.items():
#     sales.append(value)
#     book.append(key)

# print(sales)
# print(book)

# booksList = zip(book,sales)
# for t in booksList:
#     pprint(t) 
# print(sales)
# print(book)

# booksList = zip(book,sales)
# for t in booksList:
#     pprint(t) 
# import numpy 
import pandas as pd
# mydataset={
#     'cars':['BMW','Volvo','Ford','Mercedes','Audi'],
#     'passings':[3,7,2,5,10],
#     'Popularity':[11,12,13,14,15]
# }
# df=pd.DataFrame(mydataset,index=['BMW','Volvo','Ford','Mercedes','Audi'])
# print(df.loc[[BMW,Ford]])
# print(df.loc[0:3])

df=pd.read_csv('cities.csv')
#print (df)
#print(df.info())
newdf=df.dropna()
#print(newdf)
Strndf=newdf.to_string()
print(Strndf)
# print(newdf.info())
# meanVa1=df['Calories'].mean()
# medianVal=df['Calories'].median()
# modeVal=df['Calories'].mode()
# df['Calories']

# def HelloWorld():
#     print('Hello Python')
#     print ('Hello World')
# def Twice():
#     HelloWorld()
#     HelloWorld()
# Twice()

# def HW ():
#     return 'Hellooooo'
# x= HW()
# print (x)
# def printContent (*args):
#     return f'The name is {args['name']}, and surname is {args['surname']} and the Profession is {'profession'} !'
# x=printContent('Ammar','Nammour','Eng')
# y=printContent('Max','Christopher')
# z=printContent('Benni','Kindest')

# print(x,y,z,sep='\n')

# def FullName(*args):
#     return f'First name is: {args[0]} Surname is: {args[1]}'
# a=(Ammar,Nammour)
# print(FullName(a))

# def AddNumbers (*Numbers):
#     num=0
#     for x in Numbers:
#         num+=x
#     return num

# x=AddNumbers(1,2,3)
# y=AddNumbers(8,7,5,2,16,6)
# z=AddNumbers(1,2)

# print(x)
# print(y)
# print(z)


# def multiBySelf (*args):
#     multi=1
#     for x in args:
#         multi *= x
       
#     return multi 
# MyList=[10,9,6,8,7,5]
# mm=multiBySelf(*MyList)
# print(mm)

# cities=['Berlin','Paris','London','Damascus']
# x1,x2,x3,x4= cities
# def displyCities(ListOfCities):
#     return ListOfCities
# retval=displyCities(cities)
# print(retval)


# def getParity (number , parityType):
#     if parityType == 'odd':
#         return number %2 !=0
#     if parityType == 'even':
#         return number %2 ==0
#     else:
#         return 'Parity indicated is unknown'
# num= input('Enter any number you want to check it:  ')
# string=input('Enter what do you want to check: "even" or "odd":  ')
# print(f'The number {num} is {string}: ',getParity(num,string))

# import datetime

# def greet (name,date):
#     date= 0
#     condition=datetime.datetime(2021, 5, 7, 12,00, 00)
#     condition2=datetime.datetime(2021, 5, 7, 18,00, 00)
#     if condition2 > date >= condition:
#         print('Good Afternoon!',name)
#     if date > condition2:
#         print('Good Night!',name)
#     else:
#         print('Good Morning',name)
# name= input('Enter your name :)  ')
# date= datetime.datetime(2021, 5, 7, 12, 0, 1)
# greet(name,date)

# A=()
# R=int(input('Enter the number of numbers:  '))
# for x in range (R):
#     elements = input(f'Enter the value of the number {x+1}: ')
# A+=(elements,)
# print("dad",A)

# globalVar= ['Im global']

# def localVar (newString):
#     globalVar
    # newString.append('1')
    # newString.append('2')
    # globalVar1='Im local'
    # print (globalVar1)
#localVar(globalVar)
#print(globalVar)

# setting={
#     'brand' : 'Ford',
#     'model' : 'Mostang',
#     'year' :1964,
#     'whatever' : 'Ford',
#     'substring': [1,2,3,4],
#     'userProfile':{'username':'Paul', 'password': [12345,'strong']}
# }
# #print(setting)
# print(setting['substring'][-1])

# setting ={ 'Title': 'my choice '}

# def change_site_title (argument):


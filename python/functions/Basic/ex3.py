import datetime

def greet (name,date):
    date= datetime.datetime.now().time()
    condition=datetime.time(12,00)
    condition2=datetime.time(18,00)
    if condition2 > date >= condition:
        print('Good Afternoon!',name)
    if date > condition2:
        print('Good Night!',name)
    else:
        print('Good Morning',name)
name= input('Enter your name :)  ')
date= datetime.datetime.now().time()
greet(name,date)
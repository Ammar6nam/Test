# add1= lambda x:x+1
# print(add1(1))
# a= lambda x : x
# print(a('Hello world'))

# myfunc= lambda x,y:x**y
# result=myfunc(2,3)
# print(result)


# def simpFunc ():
#     return('Im simple function')
# retval = simpFunc
# print(retval)
# print(type(retval))
# print(retval())

# def wrapper(func):
#     print (func)
#     # x=func()
#     # print(10*x)

# wrapper(retval)

# def outerFunc (x):
#     x=10
#     def innerFunc():
#         print('This is inner function')+strx(x)
#     innerFunc()
#     innerFunc()

#     print(x)

# outerFunc()
# outerFunc()

# def text(text):
#     def printer():
#         print(text)
#     printer()
# pr=text('Hello World')
# pr()

# def helloDoc():
#     return 'hello Decorators!'
# def outerFunc (func):

#     def innerFunc():
#         print('This is my decoration before executing passed function')
#         message=func()
#         print(message)
#         print('This is my decoration after executing passed function')
#         return 'Test'
#     return innerFunc
    
# received=outerFunc(helloDoc)
# print(received())

# A=[2,2,3]
# num=2
# result=[x*num for x in A]
# print(result)
# Range= int(input('Enter 4 numbers please: '))
# number1=[]
# for i in range(1,Range):
#     number1.append(i)
# print(number1)

# def multiplier (n1,n2):
#     result= [n2 * x for x in n1]
#     return result

# A=[1,2,3,4,5]
# factor=2
# test=multiplier(A,factor)
# print(test)
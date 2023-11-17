#x =10
#age = 20
#if x==10 or age == 22:
#   print ("True")
#else:
#    print("Fals")
n1= float( input("1st value:  "))
n2=float( input ("2ed value:  "))
def firstFunction (n1,n2):
    sum = n1+n2
    print("Sum is: ",sum)

firstFunction(n1,n2)

def checkNumbers (n1,n2):
    if n1==n2:
        print ("Equal")
    if n1>n2:
        print (n1," bigger than ",n2)
    else:
        print (n1," lower than ",n2)
checkNumbers(n1,n2)

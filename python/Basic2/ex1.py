
print("Enter the value of the 1st int 'Should be positive'")
x=abs(int(input()))
print("Enter the value tof the 2ed int 'Should be positive'")
y=abs(int(input()))
print("The sum of:",x,"+",y,"is",x+y, sep=" ")
print("The multiple of:",x,"*",y,"is",x*y, sep=" ")
print("The division of:",x,"/",y,"is",round(x/y,2), sep=" ")
print("The reminder of:",x,"%",y,"is",x%y, sep=" ")
print("The sqrt of:",x,"is",round(x**(1/2),2), sep=" ")
print("The sqrt of:",y,"is",round(y**(1/2),2), sep=" ")
z=(x,y)
print("The Max number of your inputs is:",max(z))
print("The Min number of your inputs is:",min(z))

# a=input('Enter the value of the first number: ')
# b=input('Enter the value of the second number: ')
# c=input('Enter the value of the third number: ')
# Sum = a + b + c
# Result=Sum/3
# print(Result)

numberOfNumbers=int(input('Enter the number of numbers please: '))
number=0
sum=0
while number<numberOfNumbers:
    number +=1
    i= int(input(f'Type a integer: ({number}) '))
    sum += i
average=sum/numberOfNumbers
print(f'Average of the above numbers is: {average}')
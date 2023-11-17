num1=int(input('Enter your 1st number: '))
num2=int(input('Enter your 2ed number: '))
isOdd= lambda x:x%2 != 0
isEven= lambda x:x%2 ==0
getParity= lambda n,p : (n%2!=0) if p=='odd' else (n%2==0) if p=='even' else None

print(isOdd(num1), isEven(num1))
print(isOdd(num2), isEven(num2))
print(getParity(num1, 'odd'), getParity(num1, 'even'))
print(getParity(num2, 'odd'), getParity(num2, 'even'))
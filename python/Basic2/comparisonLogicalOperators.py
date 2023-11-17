num1=int(input('number1: '))
num2=int(input('number2: '))
if num1==num2:
    print('Numbers are not equal')
if num1>num2:
    print(f'number_{num1} is greater than number_{num2}')
else:
    print(f'number_{num2} is greater than number_{num1}')

if (num1>1000 and num2 >1000):
    print('both numbers are big','big numbers is set to True',sep='\n')
if not (num1>1000 and num2 >1000):
    print('both numbers are small','big numbers is set to False',sep='\n')




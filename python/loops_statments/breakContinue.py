number1=int(input('First number: '))
number2=int(input('Second number: '))

if number1 < number2:
    for i in range(number1,number2):
        if i % 3 ==0:
            print(f'{i} is divisible by 3')
        else:
            continue

    #print('Finished iterating from 1 to 11','...',sep='\n')

if number1 > number2:
    for j in range(number1,number2,-1):
        if j % 5 ==0 and j>0 :
            print(f'{j} is divisible by 5.')
        if j==0:
            break

elif number1 == number2:
    print('Nothing to do, both numbers are equal!')


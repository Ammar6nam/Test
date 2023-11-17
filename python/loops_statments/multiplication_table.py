number=int(input('Input a number: '))
print(f'Results of multiplication by: ({number}):',sep='\n')
n=0
while(n<10):
    n +=1
    result=number*n
    print (f'{number} x {n} = {result}')
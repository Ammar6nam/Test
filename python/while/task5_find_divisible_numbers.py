startingNumber=int(input('Type starting integer: '))
endingNumber=int(input('Type ending integer: '))
divisor=int(input('Type divisor: '))
index=startingNumber
while(index<endingNumber):
    if(index !=0 and index % divisor == 0):
        print(f'{index} is divisible by: {divisor}')
    index += 1
def getParity (number , parityType):
    if parityType == 'odd' :
        print()
        if number %2 !=0:
            return True
        else:
            return False
    if parityType == 'even':
        
        if  number %2 ==0:
            return True
        else:
            return False
    else:
        print('Parity indicated is unknown')

num= int(input('Enter any number you want to check it:  '))
string=input('Enter what do you want to check: "even" or "odd":  ')
print(f'The number {num} is {string}: ',getParity(num,string))
#print(getParity(9,'even'))
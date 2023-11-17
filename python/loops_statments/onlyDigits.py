inputs=str(input('Enter your random text: '))
counter=0
for i in inputs:
    if i.isalpha(): #if != '='
        print(f'Found a digit {counter+1}')
        counter+=1
        continue
    else:
        break

print(f'sum of digits: {counter}')
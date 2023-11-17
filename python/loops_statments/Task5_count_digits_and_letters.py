text=input('Enter the text please: ')
alpha=0
digits=0
index=0
for i in text:
    char=text[index]
    #print (char)
    if char.isalpha():
        alpha += 1
    if char.isnumeric ():
        digits +=1
    index +=1
print(f'The number of digits: {digits}',f'The number of letters: {alpha}',sep='\n')
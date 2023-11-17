text=str(input('Enter your text please: '))
letter=str(input('Enter the letter that you want to change it to capital-letter!: '))
index=0
for i in text:
    char=text[index]
    index += 1
    #print(char,end='')

    if char == letter:
        char=char.upper()
    print(char,end='')


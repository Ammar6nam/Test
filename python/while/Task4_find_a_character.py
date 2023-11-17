text=str(input('Enter your text please: '))
ltext=text.lower()
findLetter= str(input('What should be found?: '))
index=0
range1=len(text)
while (index<range1):
    char=ltext[index]
    if char == findLetter :
        print(f'Character {findLetter} found at index: {index+1}')
    index +=1

""""She came to me one morning One lonely Sunday morning Her long hair flowing in the mid-winter wind I know not how she found me For in darkness I was walking And destruction lay around me from a fight I could not win"""
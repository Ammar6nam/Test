# String= ' Overhead the albatross Hangs motionless upon the air And deep beneath the rolling waves In labyrinths of coral caves" 😃 '
# Length=len(String)
# result=' '
# index=0
# while index <=Length:
#     index+=1
#     char=String[index]
#     if char.islower():
#         char=char.upper()
#     else:
#         char=char.lower()
#     print(char,end='')
String= str(input('Enter your sentence please: '))
Length=len(String)
index=0
while(index<Length):
    char=String[index]
    index +=1
    if char.islower():
        print(char.upper(),end='')
    else:
        print(char.lower(),end='')
print(char)
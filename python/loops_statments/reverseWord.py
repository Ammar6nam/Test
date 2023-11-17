
#print(range1)
# pointers=[]
# charachters=[]
# for j in text:
#     charachters=charachters.append(j)
#     for i in range (0,range1):
#         pointers=pointers.append(i)
# charachters[j]=pointers[i]
# for x in range (-range1,0):
#     print(pointers)
#    print(j)
#for i in range (0,range1):
#    print(i)
'''  text[0]=A,1=m,2=m,3=a,4=r 
123456
 '''
# text=input('Input a text to revers: ')
# range1=len(text)
# index = 0
# result=''
# print(range1)
# for char in text[::-1] :
#     char1=text[index]
#     index += 1
#     print (char1[::-1])


# print(text[::-1])

text=str(input('Input a text to reverse: '))
result=''
for char in text[::-1]:
    result += char

print(f'Reversed word: {result}')
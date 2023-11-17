# text=(str(input('Enter your text please: ')))
# word=str(input('Which word you want to search for it? '))
# index=0
# index2=0
# a=''
# # z1=0
# c0=word[0]
# find1=text.find(word)
# length=len(text)
# lengthw=len(word)
# for x in range(0,lengthw):
#     char = text[index]
#     if text.find(word) and list(char) == list(word ):
#                 a+= text[x]
#                 index2=index
#     index +=1
# print(a)
# print(length)
# print(index2)
text=(str(input('Enter your text please: '))) #Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.'''
word=str(input('Which word you want to search for it? ')) #capital'''
if text.find(word):
    index=text.index(word)
    print(word, index)







# if z1 !=0 :
#     print(f'I found {word} at index[{y}]!')
# else:
#     print(f"I can't find {word} :( ")
# print (length)



# for i in text:
#     char=text[index]
#     index+=1
#     if word in text:
#         x=index
#print(x)
# find1=text.find(word)
# if find1 :
#     print(f'I found {word} at [index]!')
# else:
#     print(f"I can't find {word} :( ")
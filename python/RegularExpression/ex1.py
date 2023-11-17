from re import( findall,search,split,sub)
text='Berlin is a world city of culture, politics, media and science.'


first_space=text.find(' ')
mySearch= search(' ',text)
if first_space:
    print (f'The first white-space character is located at position:{first_space} ')
else:
    print('there is no space')

text2="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
findFrankfur=text.is
if findFrankfur:
    print('In this text there is a Frunkfurt word')
else:
    print('None')
    
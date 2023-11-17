from re import(
    findall,
    search,
    split,
    sub,
    IGNORECASE,)



poem= "Your children are not your children. They are the sons and daughters of Lifes longing for itself.They come through you but not from you,And though they are with you yet they belong not to you. You may give them your love but not your thoughts, For they have their own thoughts. You may house their bodies but not their souls, For their souls dwell in the house of tomorrow, which you cannot visit, not even in your dreams. You may strive to be like them, but seek not to make them like you."





myList=findall("children",poem)
mySearch= search('children',poem,)
print(mySearch)
#mySplit=split(p)
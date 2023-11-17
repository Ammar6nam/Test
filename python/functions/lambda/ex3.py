char=str(input('Enter your letter that you want to check it in the beginning of the word: '))
L = lambda x: True if (x.lower()[0].find(char))==0 else False
starts_with_p=L
Input= str(input('Enter you word: '))
print(f'The word "{Input}" starts with "{char}"? {starts_with_p(Input)}')
# print(starts_with_p("JavaScript"))
# print(starts_with_p("pirate"))

# def starts_with_p(args):
#     lower=args.lower()
#     startP=lower[0].find('p')
#     if startP:
#         return False
#     else:
#         return True
# x=starts_with_p('papa')
# print(x)


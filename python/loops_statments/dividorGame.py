i=0
j=0
while j<1:
        number1=int(input('First number: '))
        number2=int(input('second number: '))
        if number1 > 100 and number1 %2 !=0 and number2 % 2 !=0 and number1 % number2 == 0:
            i+=1
            print('you earned a point! ',' ',sep='\n')
            continue
        else:
            print("You've made a mistake!",' ',sep='\n')
        break

print (f'You gathered {i} point(s)!',' ',sep='\n')


# while i and j:
#     i=int(input('First number: '))
#     j=int(input('second number: '))
#         if i > 100 and number1 %2 !=0 and j % 2 !=0:
#             if i % j == 0:
#                 i+=1
#                 print(f'you earned a point! {i}',' ',sep='\n')
#             continue
#             else:
#                 print("You've made a mistake!",' ',sep='\n')
#             break

# print (f'You gathered {i} point(s)!')


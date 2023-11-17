def sumAll (*nums):
    num=0
    for x in nums:
        num+=x
    return num
# Range=input()
# R=int(input('Enter the number of numbers that you need to sum them: '))
# A=()
# for x in range (R):
#     elements=int(input(f'Enter the value of the number {x+1} '))
#     A += (elements,)
# print('The sum of numbers is: ', sumAll(A()))
test1 = (0, 2, 4, 5)
#test2 = [
#     [0, 2, 4, 5],
#     [6],
#     [0, 2, 4, 5, 1, 4, 3, 2]
# ]
t1=sumAll(test1)
#t2=sumAll(test2)
print(t1)
#print(t2)
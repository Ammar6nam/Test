#L= lambda numbers,factor:int(numbers())*int(factor)
#Function=L
# numbers = [2, 4, 5, 7, 9, 14]
# factor = 3
# Function(numbers,factor)
# print(Function)
# def multiple2Numbers(*args):
#     result=0
#     for x in args:
#         result *= args
#     return result
# x=multiple2Numbers(numbers,factor)
# print(x)
# factor = 2

# def multiply_numbers_by_factor(*numbers):
#     for num in numbers:
#         result = [num * factor]
#     return result

# # Test case
# numbers = [2, 4, 5, 7, 9, 14]
# result = multiply_numbers_by_factor(numbers)
# print(result)  # This will give you [4, 8, 10, 14, 18, 28]

# def multiplier (n1,n2):
#     result= [n2 * x for x in n1]
#     return result

# A=[1,2,3,4,5]
# factor=2
# test=multiplier(A,factor)
# print(test)
#result2 = multiplier(numbers,factor)
#print('Result of function way: ',result2)
L=lambda numbers,factor :  [factor * x for x in numbers]
numbers = [2, 4, 5, 7, 9, 14]
factor = int(input('Enter the values of the factor: '))
result=L(numbers,factor)
print(f'The orginal is:  {numbers}  The Result after multipling with factor:  ({factor}): is: {result}')
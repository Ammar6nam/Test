def isOdd (number):
    if number %2 !=0:
        return True
    else:
        return False
    
def isEven (number):
    if number %2 ==0:
        return True
    else:
        return False

print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))
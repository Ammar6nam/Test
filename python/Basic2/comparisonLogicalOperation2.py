input1=str(input('Enter the name of the month: '))
# list1=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# for x in list1:
#     if x == input1:
type1=[ 'january' , 'March' , 'May' , 'July' , 'September' , 'November' , 'December']
type2 = ['April' , 'June' ,'August', 'October']
type3 = ['February']


if input1 in type1:
    print('Number of the Days: 31')
if input1 in type2:
    print('Number of the Days: 30')
if input1 in type3:
    print('Number of the Days: 28')
else:
    print('you Entered wrong name ')
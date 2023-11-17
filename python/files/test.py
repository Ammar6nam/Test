import os
if os.path.exists('cities.csv'):
    print ('file is exist!')
else:
    print ('file is not exist!')
    newFile=open()
newf=open('niostats.csv','a',encoding='utf-8')
print(newf.writable())
newf.writelines
f=open('cities.csv',encoding='utf-8')
print (f)
lines=f.readlines()
print(type(lines))
for x in lines:
    print (x)

f.close
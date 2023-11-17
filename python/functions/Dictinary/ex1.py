setting = {'name' : ' Max '}
def change_site_title (args):
    setting['name']= str(args)

print(setting)
string=str(input('Enter another name! : '))
change_site_title(string)
print(setting)

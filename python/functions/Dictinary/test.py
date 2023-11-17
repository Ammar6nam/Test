# setting = {'name' : ' Max '}
# def change_site_title (args):
#     setting['name']= str(args)

# print(setting)
# string=str(input('Enter another name! : '))
# change_site_title(string)
# print(setting)

############################################

settings = {'title' : 'My original title'}

def change_site_title (args):
    settings['title']= str(args)
# print(settings)
# change_site_title("A new fancy title")
# print(settings)

default_settings={'title':' Default'}

def get_title (args):
     args=default_settings
     return args['title']


print(get_title(settings))
print(get_title())
# change_site_title("A new fancy title")
# print(get_title(setting))
# print(get_title())

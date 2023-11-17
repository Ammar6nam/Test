setting = {
    'title':'my original title',
    'pages': []
}
defultSetting = {
    'title':'my original title',
    'pages': []
}
def getPages(setting=defultSetting):
    return setting['pages']

def addPages (pages,setting=defultSetting):
    setting["pages"].append(pages)

home={
'title': 'home', 'path':'/'
}
addPages(home)
print(getPages())
print(getPages(setting))
about={'title':'about', 'path':'/about/'}
addPages(about,setting)
print(getPages())
print(getPages(setting))
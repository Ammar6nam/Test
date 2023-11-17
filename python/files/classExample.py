import json

class files:
    def __init__(self,filename:str) -> None:
        self.fileName=filename

    def update(self,tofilename:str):
        print('Updating file')

class jsonFile(files):
    def read(self):
        with open (self.fileName) as jsonFile:
            data=json.load(jsonFile)
            print(data)


    def write(self,toFilename:str,dictObj):
        with open(toFilename)as jsonFile:
            json.dump(dict)
        print('Writing to file.. ')

    def update(self,tofilName:str):
        print('updating file')
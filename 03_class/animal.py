class Animal:

    name = ''

    def __init__(self,_inName) :
        Animal.name = _inName
        self.name = _inName

    def printClassVariable(self) :
        print(Animal.name)

    def printInstanceVariable(self) :
        print(self.name)
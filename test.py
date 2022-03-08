class Dog:
    def __init__(self,name):
        self.__name = name

    def __bark(self):
        return self.__name 

    def p(self):
        return self.__bark()   
a = Dog('John')
print(a.p())
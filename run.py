from abs_class import AbstractClass

class Daughter(AbstractClass):
    def display_methods(self) -> None:
        print(self.attribute)
        
    def method_abstract(self) -> None:
        print('Implement abstract method')

daughter = Daughter()
daughter.display_methods()
daughter.method('I am here')
daughter.method_abstract()

# Error
abstractClass = AbstractClass()
abstractClass.method('Doing something')
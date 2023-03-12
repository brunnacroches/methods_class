from abc import ABC, abstractmethod

class AbstractClass():
    def __init__(self):
        self.attribute = 'Hello world'
    
    def method(self, element: str) -> None:
        print(element)
    
    @abstractmethod
    def method_abstract(self) -> None:
        pass
from abc import ABCMeta, abstractclassmethod

class Expression(metaclass=ABCMeta):
    
    @abstractclassmethod
    def reduce(self, currency: str) -> 'Money':
        pass
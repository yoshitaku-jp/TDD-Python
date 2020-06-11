from abc import ABCMeta, abstractclassmethod
from .exchanger import CurrencyExchanger

class Expression(metaclass=ABCMeta):
    
    @abstractclassmethod
    def reduce(self,bank: CurrencyExchanger, currency: str) -> 'Money':
        pass
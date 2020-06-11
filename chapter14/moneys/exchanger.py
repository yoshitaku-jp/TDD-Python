from abc import ABCMeta, abstractmethod

class CurrencyExchanger(metaclass=ABCMeta):

    @abstractmethod
    def rate(self, fromcurr: str, tocurr: str) -> int:
        pass
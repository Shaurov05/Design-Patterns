from abc import ABC, abstractmethod


class Chain(ABC):
    @abstractmethod
    def set_next_chain(self, obj: 'Chain'):
        pass

    @abstractmethod
    def calculate(self, request):
        pass

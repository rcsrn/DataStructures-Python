from abc import ABC, abstractmethod


class InOut(ABC):
    @abstractmethod
    def put(self, block = True, timeout = None):
        pass

    @abstractmethod
    def get(self):
        pass

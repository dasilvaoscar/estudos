from abc import abstractmethod, ABC

class AbstractBrowser(ABC):

    @abstractmethod
    def open(self):
        pass

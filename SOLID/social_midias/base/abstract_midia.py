from abc import abstractmethod, ABC

class AbstractMidia(ABC):

    @abstractmethod
    def get_url(self):
        pass

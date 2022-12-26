from abc import ABC

class AdapterTemplate(ABC):
  
  @staticmethod
  def create(user):
    raise NotImplementedError()
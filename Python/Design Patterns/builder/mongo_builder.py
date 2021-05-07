# Aplicação do design pattern builder

import factory

class MongoBuilder:
  
  def __init__(self):
    self._conn = factory.mongoConnection()
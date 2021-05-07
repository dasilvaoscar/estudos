# Aplicação do design pattern factory

import pymongo

mongo = pymongo.MongoClient('localhost', 27017)

def mongoConnection():
  return mongo
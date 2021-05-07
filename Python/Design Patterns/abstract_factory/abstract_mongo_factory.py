from builder.mongo_builder import MongoBuilder

# Aplicação do design pattern abstract factory

class Mongo(MongoBuilder):

  def connect(self, db):
    return self._conn[db]

  def db_names(self):
    return self._conn.list_database_names()
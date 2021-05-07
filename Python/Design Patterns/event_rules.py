# Aplicação do design pattern abstract aactory

from abstract_factory.abstract_mongo_factory import Mongo

class EventRules(Mongo):

  def __init__(self):
      super().__init__()
      self.db = self.connect()['payment-notification']

  def get_event_rules(self):
    db = self.db['reminder_rules']
    return db.find_one() 
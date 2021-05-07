# Aplicação do design pattern abstract factory

from abstract_factory.abstract_mongo_factory import Mongo

class ReminderRules(Mongo):

  def __init__(self):
      super().__init__()
      self.db = self.connect('payment-notification')

  def get_event_rules(self):
    db = self.db['reminder_rules']
    return db.find_one() 
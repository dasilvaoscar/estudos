from rules.event_rules import EventRules
from rules.reminder_rules import ReminderRules 

event_rules = EventRules().get_event_rules()
reminder_rules = ReminderRules().get_event_rules()

print(reminder_rules)

from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)
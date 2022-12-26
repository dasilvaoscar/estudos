from adapters.social_midia.template import AdapterTemplate
from base.abstract_midia import AbstractMidia

class Twitter(AbstractMidia, AdapterTemplate):

    def __init__(self, user):
        self._user = user

    def profile_info(self):
        url = 'https://twitter.com'
        return f'{url}/{self._user}' if self._user else url
    
    @staticmethod
    def create(user):
        return Twitter(user)
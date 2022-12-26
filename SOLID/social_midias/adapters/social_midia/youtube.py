from adapters.social_midia.template import AdapterTemplate
from base.abstract_midia import AbstractMidia

class Youtube(AbstractMidia, AdapterTemplate):

    def __init__(self, channel):
        self._channel = channel

    def profile_info(self):
        url = 'https://www.youtube.com'
        return f'{url}/{self._channel}' if self._channel else url
    
    @staticmethod
    def create(channel):
        return Youtube(channel)
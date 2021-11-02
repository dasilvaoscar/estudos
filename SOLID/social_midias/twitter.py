from social_midias.base.abstract_midia import AbstractMidia

class Twitter(AbstractMidia):

    def __init__(self, params):
        self._params = params

    def get_url(self):
        url = 'https://twitter.com'
        return f'{url}/{self._params}' if self._params else url
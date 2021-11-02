from social_midias.base.abstract_midia import AbstractMidia

class Youtube(AbstractMidia):

    def __init__(self, params):
        self._params = params

    def get_url(self):
        url = 'https://www.youtube.com'
        return f'{url}/{self._params}' if self._params else url
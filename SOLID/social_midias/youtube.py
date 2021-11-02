from social_midias.abstract_midia import AbstractMidia

class Youtube(AbstractMidia):

    def __init__(self, params):
        self._params = params

    def get_url(self):
        return f'https://www.youtube.com/{self._params}'
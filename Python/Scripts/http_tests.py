import requests
import os

h1 = requests.get('https://github.com/OscarSilvaOfficial')
local = os.path.abspath('file.json')

with open(local, 'w+') as f:
  f.write(str(h1.text).replace("'", '"'))
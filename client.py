from socket  import *
from constCS import * #-
from datetime import datetime
import threading
import random

# a = add, s = subtract, m = multiply, d = divide

def requisicao():
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    op = random.choice(['a','s','m','d'])

    msg = (n1,n2,op)
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT)) # connect to server (block until accepted)

        s.send(str.encode(str(msg)))
        data = s.recv(1024)

        s.close()
    
    except Exception as e:
        print(f"Deu ruim aqui: {e}")


req = 400
lista_threads = [] # guardar as threads em algum lugar

t1 = datetime.now()

for i in range(req):
    t = threading.Thread(target=requisicao)
    lista_threads.append(t)
    t.start()

for t in lista_threads:
    t.join()

t2 = datetime.now()
print(t2-t1)

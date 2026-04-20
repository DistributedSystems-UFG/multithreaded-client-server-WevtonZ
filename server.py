from socket  import *
from constCS import *
import threading

# função para tratar as informações passadas pelo cliente.
# a ideia agora é fazer com que essa função seja a principal forma de tratar o cliente na thread
# atual, e não deixar com que o laço principal la embaixo lide com isso, já que isso seria
# adicionar logica demais lá. As vezes programação orientada a objetos ajuda um pouco.
def trata_cliente(conn, addr):
	try:
		data = conn.recv(1024)
		if not data:
			return # sessão encerrada por falta de informação
		msg = bytes.decode(data)
		tpl = eval(msg)

		n1=tpl[0]
		n2=tpl[1]
		op=tpl[2]

		if op == 'a':
			return n1+n2
		elif op == 's':
			return n1-n2
		elif op == 'm':
			return n1*n2
		else:
			if n2 == 0:
				return -1
			return n1/n2
	except:
		print("deu errado")
	finally:
		conn.close()
		print("acabou a thread atual.")

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client
while True:                # forever
	res = trata_cliente(conn, addr)
	data = conn.recv(1024)   # receive data from client
	if not data: break	   # stop if client stopped

conn.send(str.encode(str(res))) # return sent data plus an "*"
conn.close()  	             # close the connection

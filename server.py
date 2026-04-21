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
		# se eu entendi corretamente, com threads, eu nao preciso mais retornar as coisas na
		# funcao. O trabalho de resolver as coisas fica com a thread. Então, eu uso a função para
		# poder resolver uma thread em particular e depois enviar a partir daqui mesmo.
		res = 0
		if op == 'a':
			res = n1+n2
		elif op == 's':
			res = n1-n2
		elif op == 'm':
			res = n1*n2
		else:
			if n2 == 0:
				res = -1
			res = n1/n2

		conn.send(str.encode(str(res)))

	except Exception as e:
		print(f"Simplesmente deu errado de algum jeito: {e}")

	finally:
		conn.close()
		print("acabou a thread atual.")

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  #-
s.listen(5)           #-
while True:                # forever
	(conn, addr) = s.accept()  # returns new socket and addr. client
	thread_cliente = threading.Thread(target = trata_cliente, args = (conn,addr))
	thread_cliente.start()

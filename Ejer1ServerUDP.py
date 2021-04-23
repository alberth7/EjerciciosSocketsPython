import socket
import time

class UDP_Server:
	paqueteRecibido = ""
	paqueteAEnviar = ""
 


	def __init__(self, ip, puerto):
		self.ipServer = ip
		self.puertoServer = puerto

	def inicio(self):
		sw=1
		hora = time.strftime("%H:%M:%S")
		fecha = time.strftime("%d/%m/%y")
		# SOCK_DGRAM: Este protocolo nos da una conexión no fiable. (UDP)
		serverSocketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		serverSocketUDP.bind((self.ipServer, self.puertoServer))
		
		print ("El servidor esta esperando para recibir...")

		while True:  
			#print("------")
			mensaje, direccionIP = serverSocketUDP.recvfrom(1024)
			if sw == 1:
				paqueteRecibido = mensaje
				print(f"paquete recibido: {direccionIP} ")
				paqueteAEnviar = (f"La hora del servidor es: {hora} y la fecha es {fecha}")
				serverSocketUDP.sendto(paqueteAEnviar.encode(), direccionIP)
				sw = 0
			else:
				sw = 1
				print("paquete descartado")
				#serverSocketUDP.close()
		
class MainUDP_Server:
	s = UDP_Server("127.0.0.1", 5012)
	s.inicio()
	
# -*-coding:Utf-8 -*
import socket
import time
import serial
import sys

HOTE = '127.0.0.1' #IP du serveur
PORT = 1248

caplight = serial.Serial('COM7', 9600)
print caplight
print "message", caplight.readline()

serv_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_soc.bind((HOTE, PORT))
serv_soc.listen(2)
print ("Le programme est a l'ecoute d'une eventuelle discussion, vous en serez averti.")

msg = 'd'

while msg != 'q':
	clt_soc, address = serv_soc.accept()
	print ("L'ordinateur", address, "veut discuter ! J'attends son message.")

	while msg != 'q':
		msg = str(clt_soc.recv(1024))
		if not msg:
			break
		if msg == 'q':
			break
		print ('\nMessage : ', msg ,'\a' + '\n\nVotre reponse :')
		caplight.write(msg)
		msgR = 'Reponse' + msg
		clt_soc.send(msgR)

clt_soc.close()
serv_soc.close()
caplight.close()
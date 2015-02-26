# -*-coding:Utf-8 -*
import socket
import time
import sys

forme = 0
couleur = 0
r = -1
g = -1
b = -1
luminosite = 0
frequence = 0
led = 1

quitter = 0

def miseEnForme(input, taille):
	if(len(input) == taille):
		return input
	while(len(input) < taille):
		input = '0' + input
	while(len(input) > taille):
		input = input[:len(input) - 1]
	return input
	
HOTE = '127.0.0.1'
PORT = 1248

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOTE, PORT))

for i in range(len(sys.argv)):
	if(sys.argv[i] == '-f'):
		forme = sys.argv[i+1]
	if(sys.argv[i] == '-c'):
		couleur = sys.argv[i+1]
	if(sys.argv[i] == '-l'):
		luminosite = sys.argv[i+1]
	#if(sys.argv[i] == '-d'):
	if(sys.argv[i] == '-v'):
		frequence = str(int(1000.0 / float(sys.argv[i+1])))
	#if(sys.argv[i] == '-m'):
	if(sys.argv[i] == '-L'):
		led = int(sys.argv[i+1])
	if(sys.argv[i] == '-q'):
		quitter = 1
	if(sys.argv[i] == '-r'):
		r = sys.argv[i+1]
	if(sys.argv[i] == '-g'):
		g = sys.argv[i+1]
	if(sys.argv[i] == '-b'):
		b = sys.argv[i+1]

if quitter == 0:		
	message = '';	
	if(r == -1 or g == -1 or b == -1):
		for num in range(0, int(led)):
			if (int(forme) == 0):
				message += miseEnForme(str(num), 1) + miseEnForme(str(couleur), 1) + miseEnForme(str(forme), 1) + miseEnForme(str(255 - int(luminosite)), 3)
			if (int(forme) > 0):
				message += miseEnForme(str(num), 1) + miseEnForme(str(couleur), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(luminosite)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
			if (int(forme) == 3):
				message += miseEnForme(str(frequence), 4)
	else:
		for num in range(0, int(led)):
			if (int(forme) == 0):
				message += miseEnForme(str(num), 1) + miseEnForme(str(0), 1) + miseEnForme(str(forme), 1) + miseEnForme(str(255 - int(r)), 3)
				message += miseEnForme(str(num), 1) + miseEnForme(str(1), 1) + miseEnForme(str(forme), 1) + miseEnForme(str(255 - int(g)), 3)
				message += miseEnForme(str(num), 1) + miseEnForme(str(2), 1) + miseEnForme(str(forme), 1) + miseEnForme(str(255 - int(b)), 3)
			if (int(forme) == 3):
				message += miseEnForme(str(num), 1) + miseEnForme(str(0), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(r)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
				message += miseEnForme(str(frequence), 4)
				message += miseEnForme(str(num), 1) + miseEnForme(str(1), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(g)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
				message += miseEnForme(str(frequence), 4)
				message += miseEnForme(str(num), 1) + miseEnForme(str(2), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(b)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
				message += miseEnForme(str(frequence), 4)
			elif (int(forme) > 0):
				message += miseEnForme(str(num), 1) + miseEnForme(str(0), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(r)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
				message += miseEnForme(str(num), 1) + miseEnForme(str(1), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(g)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)
				message += miseEnForme(str(num), 1) + miseEnForme(str(2), 1) + miseEnForme(str(forme), 1) + '255' + miseEnForme(str(255 - int(b)), 3) + miseEnForme(str(frequence), 4) + miseEnForme(str(frequence), 4)

	print ('\n','message:',message,'\a\n')

	soc.send(message)
else:
	soc.send('q')
#soc.send(sys.argv[1])
response = str(soc.recv(255))
print ('\n','response : ',response,'\a\n')

soc.close()
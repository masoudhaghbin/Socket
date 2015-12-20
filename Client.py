from socket import *
import threading

servername = gethostname()
serverport = 12000
clientsocket = socket(AF_INET , SOCK_STREAM)
clientsocket.connect((servername , serverport))


def listen(Mysocket):
	print "we are in listen area !"
	while True:
		servermessage = Mysocket.recv(1024)
		print "From Server : " , servermessage
		if(servermessage[0:10] == "NewStream#"):
			print "new Stream Recieved !"
			talk(Mysocket , "Do You Want this file ? ")
			# choice = raw_input("Do you want the file ?")
			# print "this is my choice :" , choice
		


def talk(Mysocket , option = "Enter your Command : "):
	print "option is " , option
	print "we are in talking area !"
	while True:
		Command = raw_input(option)
		Mysocket.send(Command)


threading.Thread(target=listen , args=(clientsocket,)).start()
threading.Thread(target=talk , args=(clientsocket,)).start()
	
	
# clientsocket.close()
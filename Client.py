from socket import *
servername = gethostname()
serverport = 12000
clientsocket = socket(AF_INET , SOCK_STREAM)
clientsocket.connect((servername , serverport))
while True:
	Command = raw_input("Enter your Command : ")
	clientsocket.send(Command)
	servermessage = clientsocket.recv(1024)
	print "From Server : " , servermessage
clientsocket.close()
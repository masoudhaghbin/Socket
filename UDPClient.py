from socket import *
servername = gethostname()
serverport = 12000
clientsocket = socket(AF_INET , SOCK_DGRAM)
message = raw_input('please enter your message:')
clientsocket.sendto(message , (servername , serverport))
modifiedmessage , serveraddress = clientsocket.recvfrom(2048)
print modifiedmessage
clientsocket.close()

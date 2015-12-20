from socket import *
servername = gethostname()
serverport = 12001
clientsocket = socket(AF_INET , SOCK_STREAM)
clientsocket.connect((servername , serverport))
sentence = raw_input('please enter your message:')
clientsocket.send(sentence)
modifiedmessage = clientsocket.recv(1024)
print "from server" , modifiedmessage
clientsocket.close()

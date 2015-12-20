from socket import *
serverport = 12001
serversocket = socket(AF_INET , SOCK_STREAM )
serversocket.bind((gethostname(), serverport))
serversocket.listen(1)
print "server is ready to recieve "
while True:
        connectionsocket , addr = serversocket.accept()
        sentence = connectionsocket.recv(1024)
        modifiedmessage = sentence.upper()
        connectionsocket.send(modifiedmessage)
        connectionsocket.close()
    

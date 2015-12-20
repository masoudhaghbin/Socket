from socket import *
import threading

RegisteredUsers = []
serverport = 12000
serversocket = socket(AF_INET , SOCK_STREAM )
serversocket.bind((gethostname(), serverport))
serversocket.listen(3)
print "server is running "
def register(name , socket , addr):
    flag = True
    global RegisteredUsers
    for i in range(len(RegisteredUsers)):
        if(RegisteredUsers[i][0] == name or RegisteredUsers[i][2] == addr):
            flag = False
            break
        else:
            continue
    if(flag):
        print "In register function !"
        RegisteredUsers.append([name , socket , addr])
        print "Registerd users :" ,
        print RegisteredUsers
    return flag
def Bye(addr):
    flag = False
    global RegisteredUsers
    for i in range(len(RegisteredUsers)):
        if(RegisteredUsers[i][2] == addr):
            print "deleting " , RegisteredUsers[i]
            del RegisteredUsers[i]
            flag = True
            break
        else:
            continue
    return flag 

def main(connectedsocket , addr):
    while True:
        print "in main"
        global RegisteredUsers
        clientCommand = connectedsocket.recv(1024)
        if(clientCommand[0:4] == "Reg#"):
            Clientname = clientCommand[4:]
            result = register(Clientname , connectedsocket , addr)
            print "result is " ,
            print result
            if(result):
                connectedsocket.send("Reg#OK")
                print "RegisteredUsers are :" , RegisteredUsers
            else:
                connectedsocket.send("Reg#NOK#NameUsedBeforeOrSameClient")
        elif(clientCommand[0:3] == "Bye"):
            print "main -> second elif"
            addr = connectedsocket.getpeername()
            result = Bye(addr)
            if(result):
                connectedsocket.send("Bye#OK")
                print "RegisteredUsers are :" ,RegisteredUsers
            else:
                connectedsocket.send("Reg#NOK#NotFoundInUsers")
        else:
            connectedsocket.send("Sorry! Not right now !")
        # connectedsocket.close()
        # print RegisteredUsers
   


while True:
        connectionsocket , addr = serversocket.accept()
        print "Got Connection from " , addr
        threading.Thread(target=main , args=(connectionsocket , addr)).start()
        # print "Im back here!"
        # print "Got Connection from " , addr
        # clientCommand = connectionsocket.recv(1024)
        # if(clientCommand[0:4] == "Reg#"):
        # 	Clientname = clientCommand[4:]
        # 	RegisteredUsers.append((Clientname , connectionsocket))
        # 	# print RegisteredUsers
        # 	connectionsocket.send("Registered Successfully!")
        # else:
        # 	connectionsocket.send("Sorry! Not right now !")
        # connectionsocket.close()
        # print RegisteredUsers




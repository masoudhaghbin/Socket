from socket import *
import threading

RegisteredUsers = []
serverport = 12000
serversocket = socket(AF_INET , SOCK_STREAM )
serversocket.bind((gethostname(), serverport))
serversocket.listen(3)
print "server is running "

# --------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------

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
# ---------------------------------------------------------------------------------------
def StreamRequest(addr , Filename):
    print "We are in Stream Request function !"
    flag = False
    requesterName = ""
    for i in range(len(RegisteredUsers)):
        if(RegisteredUsers[i][2] == addr):
            requesterName = RegisteredUsers[i][0]
            flag = True
            break
        else:
            continue
    print requesterName , "requested the file"
    if(flag):
        for i in range(len(RegisteredUsers)):
            if(RegisteredUsers[i][0] != requesterName):
                RegisteredUsers[i][1].send("hey bitch !")
            else:
                continue
    else:
        return flag


# ---------------------------------------------------------------------------------------
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
        elif(clientCommand[0:10] == "StreamReq#"):
            Filename = clientCommand[10:]
            addr = connectedsocket.getpeername()
            StreamRequest(addr , Filename)
        else:
            connectedsocket.send("Sorry! Not right now !")
        # connectedsocket.close()
        # print RegisteredUsers
# ----------------------------------------------------------------------------------------

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




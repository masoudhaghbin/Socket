from socket import *
import threading
from random import randint
from time import *

BUFF_SIZE = 10240
filename = ""
servername = gethostname()
serverport = 12000
UDP_Port = randint(12001 , 20000)
clientsocket = socket(AF_INET , SOCK_STREAM)
clientsocket.connect((servername , serverport))
clientUDPsocket = socket(AF_INET , SOCK_DGRAM )
clientUDPsocket.bind((servername, UDP_Port))

def listen(Mysocket):
	global BUFF_SIZE
	global filename
	# print "we are in listen area !"
	while True:
		counter1 = 0
		servermessage = Mysocket.recv(1024)
		print "From Server : " , servermessage
		if(servermessage[0:10] == "NewStream#"):
			filename = servermessage[10:]
			print "new Stream Recieved !"
			print "Do You Want this file ? "
		elif(servermessage[0:10] == "StreamReq#"):
			 print servermessage 
		elif(servermessage[0:7] == "Stream#"):
			# print "Im here in the listen function elif !"
			Next_UDP_Port = int(servermessage[7:])
			# print "Next port is ", Next_UDP_Port
			# print "filename is : " , filename
			myFile = open(filename , 'rb')
			# message = myFile.read(BUFF_SIZE)
			while(1):
				# print "sending " , message
				nowtime = time()
				message=myFile.read(BUFF_SIZE)
				# print "message is :" , message
				if not message:
					print "In the reading if !"
					break
				# if(counter1 == 0):
				# 	nowtime = time()
				# else:
				# 	counter1 += 1
				# print "first time is" , nowtime
				clientUDPsocket.sendto(message,(servername , Next_UDP_Port))
				thentime = time()
				diff = thentime - nowtime
				# print "thentime is " , thentime
				# print "diff is " , diff
				if(diff != 0):
					print "Upload rate is : " , BUFF_SIZE/(diff * 100000) , "Mbps"
			print "Got out of while"
			clientUDPsocket.sendto("##&&##" ,(servername , Next_UDP_Port))
			myFile.close()

			# print "message is :" , message
			# print "sent!"
			# choice = raw_input("Do you want the file ?")
			# print "this is my choice :" , choice
		


# def talk(Mysocket , option = "Enter your Command : "):
# 	print "option is " , option
# 	print "we are in talking area !"
# 	while True:
# 		Command = raw_input(option)
# 		Mysocket.send(Command)
def UDPfunc():
	global filename
	counter = 0
	while True:
	# print "Thread running"
		modifiedmessage , serveraddress = clientUDPsocket.recvfrom(BUFF_SIZE)
		# print "in udp listening ... :" , modifiedmessage , "-----------",modifiedmessage[0]
		# filename_got = str(UDP_Port)+filename
		gotfile = open(filename , 'wb')
		# print "before while"
		while(1):
			# print "in the while"
			# print "recieved message :" , modifiedmessage
			# if(counter == 0):
			# 	time1 = time()
			# else:
			# 	counter += 1
			time1 = time()
			# print "time1 is : " , time1
			if(modifiedmessage[0] == "##&&##"):
				print "got in the if"
				break
			gotfile.write(modifiedmessage[0])
			modifiedmessage = clientUDPsocket.recvfrom(BUFF_SIZE)
			time2 = time()
			# print "time 2 is : " , time2
			# print "Download Rate is : , time 1 : " , time1 , " time2 is :" , time2 , "difference is :" , time2 - time1 
			diff = time2 - time1
			# print "diff is :" , diff
			if(diff != 0):
				print "Upload rate is : " , BUFF_SIZE/(diff * 100000) , "Mbps" 
			
		print "Out of Recieved while!"
		# gotfile.write(modifiedmessage[0])
		gotfile.close()
		print "File is now closed!"
		clientsocket.send("GOT#")

threading.Thread(target=listen , args=(clientsocket,)).start()
threading.Thread(target=UDPfunc , args=()).start()
while True:
	# print "Enter your Command : "
	Command = raw_input()
	if(Command[0:4] == "Reg#"):
		clientsocket.send(Command)
	elif(Command[0:3] == "Bye"):
		clientsocket.send(Command)
	elif(Command[0:10] == "StreamReq#"):
		filename = Command[10:]
		clientsocket.send(Command)
	elif(Command[0:4] == "YEAH"):
		print "UDP port is :" , UDP_Port
		# print clientUDPsocket.gethostname()
		newCommand = Command + "#" + str(UDP_Port)
		clientsocket.send(newCommand)
	elif(Command[0:4] == "NOPE"):
		clientsocket.send(Command)



#threading.Thread(target=talk , args=(clientsocket,)).start()
	
	
# clientsocket.close()
##Liming Gong, code borrowed from https://www.geeksforgeeks.org/socket-programming-multi-threading-python/?ref=rp
import socket 
import argparse
import string, random
from time import sleep


def Main(): 
	port = 23456
	parser = argparse.ArgumentParser(description='Client side')
	parser.add_argument('-wait', dest="wait", default=20,type=int, help="wait time in ms")
	parser.add_argument('-length', dest="size", default=20,type=int, help="package size in byte")
	args = parser.parse_args()

	host = socket.gethostname() 
	# Define the port on which you want to connect 
	s = socket.socket()

	# connect to server on local computer 
	s.connect((host,port)) 
	num = 0
	while True: 
		message = ''.join(random.choice(string.ascii_lowercase) for _ in range(args.size))
		num +=1
		print("client sent packet "+str(num)+" size "+str(len(message)))
		s.send(message.encode('ascii')) 
		#print ("	client sent:"+message)

		# messaga received from server 
		data = s.recv(4096) 
		if data:
			print("client received packet "+str(num)+" size "+str(len(data)))
			#print('		client received:',str(data.decode('ascii'))) 
		
		print("wait "+str(args.wait)+"ms")
		sleep(0.001*args.wait)
	s.close() 

if __name__ == '__main__': 
	Main() 


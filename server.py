##Liming Gong, code modified from: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/?ref=rp

import socket 
  
# import thread module 
from _thread import *
import threading 
  
#print_lock = threading.Lock() 
  
def threaded(c, addr): 
    num = 0
    while True: 
  
        # data received from client 
        data = c.recv(4096) 
        if not data: 
            print('Empty data, exit thread') 
              
            # lock released on exit 
            #print_lock.release() 
            c.close() 
            break
        else: ##normal data
            num +=1
            print("server received packet "+str(num)+" size "+str(len(data)))
            #print("	server received/sent:",data)	
            c.send(data)  #return back the data 
            print("server sends  packet "+str(num)+" size "+str(len(data)))
  
  
  
def Main(): 
    host = "" 
  
    port = 23456
    s = socket.socket()
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port)) 
    print("server binded to port", port) 
  
    s.listen(5) 
    print("server is listening") 
  
    while True: 
        c, addr = s.accept() 
  
        # lock acquired by client 
        #print_lock.acquire() 
        print('new connection to :', addr) 
  
        # Start a new thread and return its identifier 
        #start_new_thread(threaded, (c,)) 
        t = threading.Thread(target=threaded,args=(c,addr))
        t.start()
        #t.join()
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 

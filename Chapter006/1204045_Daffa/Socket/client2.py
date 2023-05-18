import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Pizza order!'.encode())
with open('received.txt','wb') as f:
    print ('Order accepted')
    while True :
        print ('receive orders')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Succeed to order a pizza')
s.close()
print ('End the process')

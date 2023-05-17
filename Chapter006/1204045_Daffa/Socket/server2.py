# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Waiting for order')
while True :
    conn,addr=s.accept()
    print ('Processing the order')
    data=conn.recv(1024)
    print ('Receive orders',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Sending',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Successfully processed the order')
        conn.send('->Your order has been processed'.encode())
        conn.close()

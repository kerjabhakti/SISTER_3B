# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Server melakukan proses data surat....')
while True :
    conn,addr=s.accept()
    print ('',addr)
    data=conn.recv(1024)
    print ('Server berhasil mendapatkan data surat',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Sent',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Pengiriman data surat berhasil')
        conn.send('->Terimakasih sudah mengirim surat !'.encode())
        conn.close()

# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Menunggu permintaan')
while True :
    conn,addr=s.accept()
    print ('Memproses permintaan')
    data=conn.recv(1024)
    print ('Permintaan diterima',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Mengirim',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil melakukan proses')
        conn.send('->Permintaan Anda telah berhasil diproses'.encode())
        conn.close()

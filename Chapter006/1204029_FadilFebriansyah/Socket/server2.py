# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Menunggu Makanan')
while True :
    conn,addr=s.accept()
    print ('Memproses Makanan')
    data=conn.recv(1024)
    print ('Makanan diterima',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Mengirim',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil Memproses')
        conn.send('->Makanan anda sedang di proses ya'.encode())
        conn.close()

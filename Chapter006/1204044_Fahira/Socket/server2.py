# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Menunggu peminjaman buku')
while True :
    conn,addr=s.accept()
    print ('Memproses pinjaman buku')
    data=conn.recv(1024)
    print ('Peminjaman buku diterima',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Memproses',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil Meminjamkan Buku')
        conn.send('->Peminjaman buku telah selesai diproses'.encode())
        conn.close()

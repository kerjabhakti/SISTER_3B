# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Menunggu pesanan')
while True :
    conn,addr=s.accept()
    print ('Memproses pesanan')
    data=conn.recv(1024)
    print ('Pesanan diterima',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Mengirim',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil Memproses')
        conn.send('->Pesanan anda sudah di proses ya'.encode())
        conn.close()

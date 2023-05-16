# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Server sedang memproses data....')
while True :
    conn,addr=s.accept()
    print ('mendapatkan koneksi dari player dengan address',addr)
    data=conn.recv(1024)
    print ('Server berhasil mendapatkan data player',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Sent',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil mengirim data player')
        conn.send('->Nuhun sudah login!'.encode())
        conn.close()

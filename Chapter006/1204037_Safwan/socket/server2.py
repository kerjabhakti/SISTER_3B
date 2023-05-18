# server .py

import socket
port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(15)
print('Sedang Mengantri Proses')
while True:
    conn, addr = s.accept()
    print('Melakukan Proses Joki')
    data = conn.recv(1024)
    print('Proses Joki Berhasil', repr(data.decode()))
    filename = 'mytext.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Mmberikan Pemberitahuan', repr(l.decode()))
        l = f.read(1024)
        f.close()
        print('Joki Sudah Beres')
        conn.send('->Proses Joki Anda Telah Selesai, Makasih Kaka'.encode())
        conn.close()

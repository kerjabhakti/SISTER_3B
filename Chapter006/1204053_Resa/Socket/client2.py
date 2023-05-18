import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Tiket Bandros Rute Pink!'.encode())
with open('received.txt','wb') as f:
    print ('permintaan di proses')
    while True :
        print ('menerima pesanan tiket')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil memesan tiket bandros')
s.close()
print ('Loket ditutup!')

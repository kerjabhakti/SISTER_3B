import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Pinjam Buku Programming GO'.encode())
with open('received.txt','wb') as f:
    print ('Peminjaman buku sedang diproses')
    while True :
        print ('Buku telah berhasil dipinjam')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Buku siap dipinjam!')
s.close()
print ('peminjaman selesai')

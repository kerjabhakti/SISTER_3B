import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Selamat Datang Prajurit!'.encode())
with open('received.txt','wb') as f:
    print ('membuka data player')
    while True :
        print ('Menerima Data Prajurit...')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil mendapatkan data prajurit')
s.close()
print ('Koneksi ditutup!')

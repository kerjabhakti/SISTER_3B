import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Pesan makanan gehu pedas ya gaes!'.encode())
with open('received.txt','wb') as f:
    print ('makanan diterima')
    while True :
        print ('menerima makananan')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Sudah menerima makanan')
s.close()
print ('Menutup proses')

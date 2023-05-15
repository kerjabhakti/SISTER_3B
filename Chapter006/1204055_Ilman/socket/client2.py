import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Pesan tiket Dragon Ball Z!'.encode())
with open('received.txt','wb') as f:
    print ('pesan diterima')
    while True :
        print ('menerima pesanan')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil memesan tiket')
s.close()
print ('Menutup proses')

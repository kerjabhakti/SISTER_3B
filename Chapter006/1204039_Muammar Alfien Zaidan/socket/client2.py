import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Permintaan kartu member Wahana All in One'.encode())
with open('received.txt','wb') as f:
    print ('permintaan diterima')
    while True :
        print ('menerima permintaan')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil meminta kartu member')
s.close()
print ('Menutup proses')

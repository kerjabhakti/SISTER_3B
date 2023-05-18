import socket
s = socket.socket()
host = socket.gethostname()
port = 60000
s.connect((host, port))
s.send('Order Joki Paket Epic Abadi To Mythic'.encode())
with open('received.txt', 'wb') as f:
    print('Order Paket Joki Di Catat')
    while True:
        print('Order Paket Dalam Proses')
        data = s.recv(1024)
        if not data:
            break
        print('Data=>', data.decode())
        # write data to a file
        f.write(data)
f.close()
print('Paket Joki Berhasil Di Proses')
s.close()
print('Proses Joki selesai')

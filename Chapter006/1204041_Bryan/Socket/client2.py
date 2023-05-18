import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Melakukan Pembelian Membership The Lookouts '.encode())
with open('received.txt','wb') as f:
    print ('pembelian diterima')
    while True :
        print ('menerima pembelian')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil membership')
s.close()
print ('Sampai Jumpa bulan depan!')

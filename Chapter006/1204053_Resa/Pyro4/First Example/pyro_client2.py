import Pyro4

uri = "PYRO:obj_509df783b123459eb87863913be735a2@localhost:49729" 

filename = "mytext.txt"  # Ganti dengan nama file yang ingin Anda kirim

fileserver = Pyro4.Proxy(uri)
file_content = fileserver.send_file(filename)

# Konversi file_content menjadi bytesimport Pyro4

uri = "PYRO:obj_509df783b123459eb87863913be735a2@localhost:49729"  

filename = "mytext.txt"  

fileserver = Pyro4.Proxy(uri)
file_content = fileserver.send_file(filename)

# Konversi file_content menjadi bytes dengan encoding UTF-8
file_content_bytes = file_content.encode('utf-8')

with open("received_file.txt", "wb") as file:
    file.write(file_content_bytes)

print("File berhasil diterima.")
file_content_bytes = bytes(file_content)

with open("mytext.txt", "wb") as file:
    file.write(file_content_bytes)

print("File berhasil diterima.")
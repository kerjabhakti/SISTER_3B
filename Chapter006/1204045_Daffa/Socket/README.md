# Tema Client Server 1: Login ke website restaurant

File "server.py" merupakan file yang berperan sebagai server. Di dalam file ini, kita membuat objek socket menggunakan modul socket, mengikatnya ke alamat host dan port tertentu, lalu menerima koneksi masuk. Setiap kali ada koneksi masuk, kita menerima koneksi tersebut dan mencetak informasi tentang pengguna yang terhubung. Selanjutnya, kita mengirimkan waktu saat ini ke klien dan menutup koneksi.

File "client.py" adalah file yang berperan sebagai klien. Di dalam file ini, kita membuat objek socket menggunakan modul socket, kemudian terhubung ke server menggunakan alamat host dan port yang sama. Setelah terhubung, kita menerima data dari server, yaitu waktu saat ini, dan mencetak pesan selamat datang beserta waktu tersebut. Setelah itu, kita menutup koneksi.

# Menjalankan Program 1

1. Menjalankan program server1
```python
py server.py
```


2. Menjalakan program client1
```python
py client.py
```



# Tema Client Server 2: Proses Pemesanan Makanan

File "server2.py" adalah file yang bertindak sebagai server. Di dalam file ini, kita membuat objek soket menggunakan modul soket, mengikatkannya ke alamat host dan port tertentu, dan kemudian mendengarkan koneksi masuk. Setiap kali ada koneksi masuk, kita menerima pesan dari klien, membaca isi file "mytext.txt", dan mengirimkannya kembali ke klien. Setelah semua data terkirim, kita mengirim pesan konfirmasi ke klien dan menutup koneksi.

File "client2.py" adalah file yang bertindak sebagai klien. Di dalam file ini, kita membuat objek soket menggunakan modul soket dan terhubung ke server menggunakan alamat host dan port yang sama. Kemudian, kita mengirim pesan "Pizza order!" ke server. Setelah itu, kita menerima data dari server dan menuliskannya ke file "received.txt". Setelah semua data diterima, kita menutup koneksi.

# Menjalankan Program 2

1. Menjalankan program server1
```python
py server2.py
```


2. Menjalakan program client1
```python
py client2.py
```


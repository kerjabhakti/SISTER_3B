# Tema Client Server 1: Login website Terlarang

File "server.py" adalah file yang berfungsi sebagai server. Dalam file ini, kita membuat socket objek menggunakan socket module, mengikatnya ke alamat host dan port tertentu, dan kemudian menerima koneksi masuk. Setiap kali ada koneksi masuk, kita menerima koneksi tersebut dan mencetak informasi tentang pengguna yang terhubung. Selanjutnya, kita mengirimkan waktu saat ini ke klien dan menutup koneksi.

File "client.py" adalah file yang berfungsi sebagai klien. Dalam file ini, kita membuat socket objek menggunakan socket module, dan kemudian kita terhubung ke server menggunakan alamat host dan port yang sama. Setelah terhubung, kita menerima data dari server, yaitu waktu saat ini, dan mencetak pesan selamat datang bersama dengan waktu tersebut. Setelah itu, kita menutup koneksi.

# Menjalankan Program 1

1. Menjalankan program server1
```python
py server.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/dc2c70e2-fa98-4365-bff2-5d14f8ce2137)

2. Menjalakan program client1
```python
py client.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/f0bb764d-fe5f-47e4-b1be-140854acf007)


# Tema Client Server 2: Proses Pemesanan Tiket

File "server2.py" adalah file yang berfungsi sebagai server. Dalam file ini, kita membuat socket objek menggunakan socket module, mengikatnya ke alamat host dan port tertentu, dan kemudian mendengarkan koneksi masuk. Setiap kali ada koneksi masuk, kita menerima pesan dari klien, membaca file "mytext.txt", dan mengirimkan isinya ke klien. Setelah semua data terkirim, kita mengirimkan pesan konfirmasi ke klien dan menutup koneksi.

File "client2.py" adalah file yang berfungsi sebagai klien. Dalam file ini, kita membuat socket objek menggunakan socket module dan terhubung ke server menggunakan alamat host dan port yang sama. Kemudian, kita mengirim pesan "Pesan tiket Dragon Ball Z!" ke server. Setelah itu, kita menerima data dari server dan menulisnya ke file "received.txt". Setelah semua data diterima, kita menutup koneksi.

# Menjalankan Program 2

1. Menjalankan program server1
```python
py server2.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/c0abc3a7-cb41-4f1d-8a80-e866483cd6c1)


2. Menjalakan program client1
```python
py client2.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/4a579636-e0f8-4a1d-8b5b-a86f342cacef)

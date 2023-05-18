# Tema Client Server 1: Login ke Tempat Pembelian Membership

- File "server.py" berfungsi sebagai server. Di dalam file ini, kita membuat objek socket menggunakan modul socket, mengikatnya ke alamat host dan port tertentu, lalu menerima koneksi masuk. Setiap kali ada koneksi masuk, kita menerima koneksi tersebut dan mencetak informasi tentang pengguna yang terhubung. Selanjutnya, kita mengirimkan waktu saat ini ke klien dan menutup koneksi.

- File "client.py" berperan sebagai klien. Di dalam file ini, kita membuat objek socket menggunakan modul socket, kemudian terhubung ke server menggunakan alamat host dan port yang sama. Setelah terhubung, kita menerima data dari server, yaitu waktu saat ini, dan mencetak pesan selamat datang beserta waktu tersebut. Setelah itu, kita menutup koneksi.

# Menjalankan Program 1

1. Menjalankan program server1
```python
py server.py
```
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/Screenshot%202023-05-18%20232620.png)


2. Menjalakan program client1
```python
py client.py
```
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/Screenshot%202023-05-18%20232631.png)


# Tema Client Server 2: Proses Pembelian Membership

- File "server2.py" berfungsi sebagai server. Di dalam file ini, kita membuat objek socket menggunakan modul socket, mengikatkannya ke alamat host dan port tertentu, dan kemudian mendengarkan koneksi masuk. Setiap kali ada koneksi masuk, kita menerima pesan dari klien, membaca isi file "mytext.txt", dan mengirimkannya kembali ke klien. Setelah semua data terkirim, kita mengirim pesan konfirmasi ke klien dan menutup koneksi.

- File "client2.py" berperan sebagai klien. Di dalam file ini, kita membuat objek socket menggunakan modul socket dan terhubung ke server menggunakan alamat host dan port yang sama. Selanjutnya, kita mengirim pesan "Pizza order!" ke server. Setelah itu, kita menerima data dari server dan menuliskannya ke file "received.txt". Setelah semua data diterima, kita menutup koneksi.
# Menjalankan Program 2

1. Menjalankan program server1
```python
py server2.py
```
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/Screenshot%202023-05-18%20232738.png)


2. Menjalakan program client1
```python
py client2.py
```
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/Screenshot%202023-05-18%20232752.png)

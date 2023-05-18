# Tema Client Server 1: Login ke website restaurant

File "server.py" merupakan file yang berperan sebagai server. Di dalam file ini, kita membuat objek socket menggunakan modul socket, mengikatnya ke alamat host dan port tertentu, lalu menerima koneksi masuk. Setiap kali ada koneksi masuk, kita menerima koneksi tersebut dan mencetak informasi tentang pengguna yang terhubung. Selanjutnya, kita mengirimkan waktu saat ini ke klien dan menutup koneksi.

File "client.py" adalah file yang berperan sebagai klien. Di dalam file ini, kita membuat objek socket menggunakan modul socket, kemudian terhubung ke server menggunakan alamat host dan port yang sama. Setelah terhubung, kita menerima data dari server, yaitu waktu saat ini, dan mencetak pesan selamat datang beserta waktu tersebut. Setelah itu, kita menutup koneksi.

# Menjalankan Program 1

1. Menjalankan program server1
```python
py server.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/9087fda2-bc22-46f8-ab6e-a3b6d1446965)


2. Menjalakan program client1
```python
py client.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/89caeb99-7203-49e0-bee4-c2affbbe8beb)


# Tema Client Server 2: Proses Pemesanan Makanan

File "server2.py" adalah file yang bertindak sebagai server. Di dalam file ini, kita membuat objek soket menggunakan modul soket, mengikatkannya ke alamat host dan port tertentu, dan kemudian mendengarkan koneksi masuk. Setiap kali ada koneksi masuk, kita menerima pesan dari klien, membaca isi file "mytext.txt", dan mengirimkannya kembali ke klien. Setelah semua data terkirim, kita mengirim pesan konfirmasi ke klien dan menutup koneksi.

File "client2.py" adalah file yang bertindak sebagai klien. Di dalam file ini, kita membuat objek soket menggunakan modul soket dan terhubung ke server menggunakan alamat host dan port yang sama. Kemudian, kita mengirim pesan "Pizza order!" ke server. Setelah itu, kita menerima data dari server dan menuliskannya ke file "received.txt". Setelah semua data diterima, kita menutup koneksi.

# Menjalankan Program 2

1. Menjalankan program server1
```python
py server2.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/8e91eeb1-3f85-414b-9b7c-51f7f3cf9df2)


2. Menjalakan program client1
```python
py client2.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/8ffda0e7-6f51-4ae1-860a-c54fc237df30)

# Tema: Membership Youtube !

- File "pyro_client.py" berfungsi sebagai klien yang digunakan untuk berkomunikasi dengan server Pyro. Di dalamnya, kita menggunakan Pyro4 untuk membuat proxy ke objek server dan memanggil metode "welcomeMessage" dengan memberikan nama film sebagai argumen.

- File "pyro_server.py" berperan sebagai server Pyro. Di dalamnya, kita mendefinisikan kelas "Server" yang memiliki metode "welcomeMessage" yang akan dipanggil oleh klien. Metode ini mengembalikan pesan sambutan yang mencakup nama film yang diberikan oleh klien.

-Untuk menjalankan aplikasi ini, pastikan Pyro4 telah terinstal. Anda perlu menjalankan server Pyro terlebih dahulu menggunakan file "pyro_server.py" untuk mendaftarkan objek server di name server Pyro. Setelah itu, jalankan file "pyro_client.py" untuk berinteraksi dengan server dan mendapatkan pesan sambutan.

# Menjalankan Program
1. Nyalakan server pyro terlebih dahulu

```python
python -m Pyro4.naming
```

2. Jalankan server

```python
py pyro_server.py
```

3. Jalankan client dan ikutin perintahnya

```python
py pyro_client.py
```

# Output Program

1. Menjalankan server pyro4
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/pyro_1.png)

2. Server
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/pyro_2.png)

3. Client
![image](https://raw.githubusercontent.com/BryanFlava/asset-gambar/main/SISTER%20OUTPUT/Chapter006/pyro_3.png)


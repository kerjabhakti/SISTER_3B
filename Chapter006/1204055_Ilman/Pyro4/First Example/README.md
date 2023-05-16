# Tema: Pemasanan Tiket

File "pyro_client.py" adalah file yang berfungsi sebagai client untuk berkomunikasi dengan server Pyro. Di dalamnya, kita menggunakan Pyro4 untuk membuat proxy ke objek server dan memanggil metode "welcomeMessage" dengan memberikan nama film sebagai argumen.

File "pyro_server.py" adalah file yang berfungsi sebagai server Pyro. Di dalamnya, kita mendefinisikan kelas "Server" yang memiliki metode "welcomeMessage" yang akan dipanggil oleh client. Metode ini mengembalikan pesan sambutan yang mencakup nama film yang diberikan oleh client.

Untuk menjalankan aplikasi ini, pastikan Anda telah menginstal Pyro4. Anda perlu menjalankan server Pyro menggunakan file "pyro_server.py" terlebih dahulu untuk mendaftarkan objek server di name server Pyro. Setelah itu, Anda dapat menjalankan file "pyro_client.py" untuk berinteraksi dengan server dan mendapatkan pesan sambutan.

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

# Hasil Program

1. Menjalankan server pyro4
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/8d8bfb86-070a-448e-b6a2-09d53bf580aa)

2. Server
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/b4325295-c2d7-41c4-9470-9b2b611dd9cc)

3. Client
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/64587e22-db4d-4796-9fc0-d7ab4909d100)

# Tema: Food Orders

File "pyro_client.py" berperan sebagai klien yang digunakan untuk berkomunikasi dengan server Pyro. Di dalamnya, kami menggunakan Pyro4 untuk membuat proxy ke objek server dan memanggil metode "welcomeMessage" dengan memberikan nama film sebagai argumen.

File "pyro_server.py" bertindak sebagai server Pyro. Di dalamnya, kami mendefinisikan kelas "Server" yang memiliki metode "welcomeMessage" yang akan dipanggil oleh klien. Metode ini mengembalikan pesan sambutan yang mencakup nama film yang diberikan oleh klien.

Untuk menjalankan aplikasi ini, pastikan Pyro4 telah diinstal. Anda perlu menjalankan server Pyro terlebih dahulu menggunakan file "pyro_server.py" untuk mendaftarkan objek server di name server Pyro. Setelah itu, jalankan file "pyro_client.py" untuk berinteraksi dengan server dan mendapatkan pesan sambutan.

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
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/d64f9f86-628e-44b0-a598-238cc36b814d)

2. Server
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/c87e707c-8a5e-4653-a9a1-8e59e3675277)

3. Client
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/f7d1b1c7-fc42-4336-a528-1908c871c03a)


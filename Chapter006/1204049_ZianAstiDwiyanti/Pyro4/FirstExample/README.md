# Pyro4 - First Example
## Studi Kasus : Surat
Pada file "pyro_client.py", kita menggunakan Pyro4 untuk membuat proxy yang terhubung ke server. Kode ini meminta pengguna untuk memasukkan pesan (isi) sebagai input. Setelah itu, kita menggunakan proxy untuk memanggil metode "welcomeMessage" pada server dan memberikan pesan tersebut sebagai argumen. Hasil balasan dari server akan dicetak.

Pada file "pyro_server.py", kita mendefinisikan kelas "Server" yang mengimplementasikan server Pyro. Metode "welcomeMessage" pada kelas tersebut didekorasi dengan "@Pyro4.expose" agar dapat diakses dari jarak jauh. Metode ini menerima argumen "isi" yang merupakan pesan yang diterima dari client. Kemudian, server akan mengembalikan balasan berupa string yang berisi pesan "From Zian: " diikuti dengan isi dari pesan yang diterima.

# Output Program
```python
python -m Pyro4.naming
```
![naming](https://github.com/Zianasti/SISTER_3B/assets/79962655/29bf8c7c-8e70-4300-9f24-c8a4c3a19b60)

```python
python pyro_server.py
```
![pyro_server](https://github.com/Zianasti/SISTER_3B/assets/79962655/589ad0eb-6d6b-45c0-827e-3e253f0b17e8)

```python
python pyro_client.py
```
![pyro client](https://github.com/Zianasti/SISTER_3B/assets/79962655/5b8337e8-dcab-442e-a81c-6ef4c9396b47)


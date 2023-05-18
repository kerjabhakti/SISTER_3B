# Studi Kasus : Proses Surat
Studi kasus ini melibatkan penggunaan Pyro4 untuk mengimplementasikan komunikasi jarak jauh antara beberapa server yang membentuk sebuah topologi rantai, dengan konsep metafora "surat". Setiap server dalam rantai akan menerima pesan, memprosesnya, dan meneruskannya ke server berikutnya hingga mencapai tujuan akhir.

Pada file "chainTopology.py", terdapat kelas "Chain" yang didekorasi dengan "@Pyro4.expose" agar dapat diakses dari jarak jauh. Kelas ini memiliki metode "init" yang menginisialisasi nama objek, nama server saat ini, dan objek server saat ini. Metode "process" digunakan untuk memproses pesan. Jika objek server saat ini belum diinisialisasi, maka akan dibuat proxy ke objek server yang sesuai dengan nama. Jika nama objek terdapat dalam pesan, maka server selesai dan mengembalikan pesan selesai. Jika tidak, pesan akan diteruskan ke objek server berikutnya untuk diproses.

Pada file "client_chain.py", terdapat kelas "Chain" yang juga didekorasi dengan "@Pyro4.expose" agar dapat diakses dari jarak jauh. Kelas ini memiliki metode "init" dan "process" yang mirip dengan kelas "Chain" pada file "chainTopology.py". Metode "process" digunakan untuk mengirimkan pesan ke server dan menerima balasan.

Pada file "server_chain_1.py", kita membuat objek server Pyro dengan menggunakan kelas "Chain" dari file "chainTopology.py". Objek tersebut didaftarkan dalam name server menggunakan Pyro4.locateNS() dan ns.register(). Setelah itu, daemon.requestLoop() digunakan untuk memulai event loop server agar dapat menerima pemanggilan dari client.

Pada file "chain_server_2.py" dan "chain_server_3.py", langkah-langkah yang sama seperti pada "server_chain_1.py" dilakukan untuk membuat objek server dan mendaftarkannya dalam name server.

# Output Program
```python
python -m Pyro4.naming
```
![namin2](https://github.com/Zianasti/SISTER_3B/assets/79962655/1f5adc65-b996-4a10-851f-3a52f78732a5)

```python
python server_chain_1.py
```
![s chain1](https://github.com/Zianasti/SISTER_3B/assets/79962655/787eb9b7-00c2-448d-91c4-9c4815757923)

```python
python server_chain_2.py
```
![s chain2](https://github.com/Zianasti/SISTER_3B/assets/79962655/ecebd512-ad15-4780-b0c9-14611fb2dd1a)

```python
python server_chain_3.py
```
![s chain3](https://github.com/Zianasti/SISTER_3B/assets/79962655/90f3ad86-1dfb-4f82-9064-8e98f4abd8d6)

```python
python client_chain.py
```
![client chain](https://github.com/Zianasti/SISTER_3B/assets/79962655/79d9d2ff-dcc7-4f37-b5c8-bec6e69f5fa8)

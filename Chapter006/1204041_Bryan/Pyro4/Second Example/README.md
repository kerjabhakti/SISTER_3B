# Tema: Proses Pembelian Membership

- File "chainTopology.py" memuat definisi kelas Chain yang memiliki fungsi process. Fungsi ini digunakan untuk memproses pesan dalam suatu rantai topologi. Setiap objek Chain memiliki nama dan nama server saat ini, serta mampu memanggil fungsi process pada server berikutnya dalam rantai.

- File "client_chain.py" berperan sebagai klien yang berinteraksi dengan objek Chain. Di dalamnya, kita membuat proxy ke objek Chain menggunakan Pyro4 dan memanggil fungsi process dengan menyediakan pesan sebagai argumen.

- File "server_chain_1.py", "server_chain_2.py", dan "server_chain_3.py" bertindak sebagai server dalam rantai topologi. Setiap server membuat objek Chain dengan mengatur server saat ini dan server berikutnya dalam rantai. Objek tersebut didaftarkan di name server Pyro menggunakan Pyro4, dan kemudian server akan memasuki loop permintaan untuk menerima panggilan dari klien.

# Menjalankan Program

1. Nyalakan server Pyro4

```python
python -m Pyro4.naming
```
![image]()

2. Menyalakan server chain 1, 2 dan 3

```python
py server_chain_1.py
```
![image]()


```python
py server_chain_2.py
```
![image]()


```python
py server_chain_3.py
```
![image]()


3. Menjalankan program client

```python
py client_chain.py
```
![image]()


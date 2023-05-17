# Tema: Proses Pemutaran Film

File "chainTopology.py" berisi definisi kelas Chain yang memiliki metode process. Metode ini digunakan untuk mengolah pesan dalam sebuah rantai topologi. Setiap objek Chain memiliki nama dan nama server saat ini, serta dapat memanggil metode process pada server berikutnya dalam rantai.

File "client_chain.py" berperan sebagai klien yang digunakan untuk berinteraksi dengan objek Chain. Di dalamnya, kami membuat proxy ke objek Chain menggunakan Pyro4 dan memanggil metode process dengan menyediakan pesan sebagai argumen.

File "server_chain_1.py", "server_chain_2.py", dan "server_chain_3.py" berfungsi sebagai server dalam rantai topologi. Setiap server membuat objek Chain dengan mengatur server saat ini dan server berikutnya dalam rantai. Objek tersebut didaftarkan di name server Pyro menggunakan Pyro4, dan kemudian server akan memasuki loop permintaan untuk menerima panggilan dari klien.

# Menjalankan Program

1. Nyalakan server Pyro4

```python
python -m Pyro4.naming
```

2. Menyalakan server chain 1, 2 dan 3

```python
py server_chain_1.py
```


```python
py server_chain_2.py
```


```python
py server_chain_3.py
```


3. Menjalankan program client

```python
py client_chain.py
```


# Tema: Proses Pemutaran Film

File "chainTopology.py" adalah file yang mendefinisikan kelas Chain yang memiliki metode process. Metode ini digunakan untuk memproses pesan dalam sebuah rantai topologi. Setiap objek Chain memiliki nama dan nama server saat ini, serta memiliki kemampuan untuk memanggil metode process pada server berikutnya dalam rantai

File "client_chain.py" adalah file yang berfungsi sebagai client untuk berinteraksi dengan objek Chain. Di dalamnya, kita membuat proxy ke objek Chain dengan menggunakan Pyro4 dan memanggil metode process dengan menyediakan pesan sebagai argumen.

File "server_chain_1.py", "server_chain_2.py", dan "server_chain_3.py" adalah file-file yang berfungsi sebagai server dalam rantai topologi. Setiap server akan membuat objek Chain dengan mengatur server saat ini dan server berikutnya dalam rantai. Objek tersebut akan didaftarkan di name server Pyro menggunakan Pyro4, dan kemudian server akan memasuki loop permintaan untuk menerima panggilan dari client.

# Menjalankan Program

1. Nyalakan server Pyro4

```python
python -m Pyro4.naming
```

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/df5799fa-7462-4755-9205-748e38454d09)

2. Menyalakan server chain 1, 2 dan 3

```python
py server_chain_1.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/04b7fbaf-5306-430b-baac-21b68dce924b)


```python
py server_chain_2.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/4705554f-620d-4692-a0f5-6fb99d6b11b0)

```python
py server_chain_3.py
```
![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/75b7a33e-965c-4f3d-8107-f7d36964e656)

3. Menjalankan program client

```python
py client_chain.py
```

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/8408ea5e-209a-48f7-9644-75c6629ffa68)

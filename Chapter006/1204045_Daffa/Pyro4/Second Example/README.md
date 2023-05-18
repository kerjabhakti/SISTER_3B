# Tema: Proses Pemesanan Makanan

File "chainTopology.py" berisi definisi kelas Chain yang memiliki metode process. Metode ini digunakan untuk mengolah pesan dalam sebuah rantai topologi. Setiap objek Chain memiliki nama dan nama server saat ini, serta dapat memanggil metode process pada server berikutnya dalam rantai.

File "client_chain.py" berperan sebagai klien yang digunakan untuk berinteraksi dengan objek Chain. Di dalamnya, kami membuat proxy ke objek Chain menggunakan Pyro4 dan memanggil metode process dengan menyediakan pesan sebagai argumen.

File "server_chain_1.py", "server_chain_2.py", dan "server_chain_3.py" berfungsi sebagai server dalam rantai topologi. Setiap server membuat objek Chain dengan mengatur server saat ini dan server berikutnya dalam rantai. Objek tersebut didaftarkan di name server Pyro menggunakan Pyro4, dan kemudian server akan memasuki loop permintaan untuk menerima panggilan dari klien.

# Menjalankan Program

1. Nyalakan server Pyro4

```python
python -m Pyro4.naming
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/155b83ce-9017-40ed-91d9-a3d961143088)

2. Menyalakan server chain 1, 2 dan 3

```python
py server_chain_1.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/4907058d-737a-43ec-a34a-9622885c00ea)


```python
py server_chain_2.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/c6c6ba32-bf29-42ba-933a-a80678298a35)


```python
py server_chain_3.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/db090d7e-5367-4cf5-bdad-01d9104c358c)


3. Menjalankan program client

```python
py client_chain.py
```
![image](https://github.com/daulJsx/SISTER_3B/assets/112412781/b69a04d2-174a-44d4-84d2-99eff721a51b)


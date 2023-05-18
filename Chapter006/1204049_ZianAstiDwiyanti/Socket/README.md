# Studi Kasus : Surat
## Program 1
Client berperan sebagai pengirim surat yang mengirimkan permintaan ke server, sedangkan server berperan sebagai penerima surat yang menerima permintaan dan memberikan respons. Socket digunakan untuk menghubungkan kedua entitas ini sehingga dapat saling berkomunikasi. Client membuat socket dan menghubungkannya ke alamat server (host dan port), kemudian menerima respons dari server. Server membuat socket, melakukan binding ke alamat yang ditentukan, dan menunggu koneksi masuk. Ketika ada koneksi masuk dari client, server menerima permintaan dan memberikan respons yang berupa waktu saat ini. Setelah itu, koneksi socket ditutup.

## Output Program 1
```python
python server.py
```
![socket server1](https://github.com/Zianasti/SISTER_3B/assets/79962655/af4b568e-eb61-4183-a668-726242e928b5)
```python
python client.py
```
![socket1](https://github.com/Zianasti/SISTER_3B/assets/79962655/e31fb624-a70e-4392-bb84-ecefca97002a)

## Program 2
 Client2 berperan sebagai pengirim surat yang menghubungkan socket ke server, mengirimkan pesan surat, dan menerima data surat dari server. Client2 juga membuka file "received.txt" untuk menulis isi surat yang diterima. Server2 berperan sebagai penerima surat yang melakukan binding socket, mendengarkan koneksi masuk, menerima pesan surat dari client2, membuka file "mytext.txt" untuk membaca isi surat, dan mengirimkan isi surat kepada client2. Setelah selesai mengirim surat, server2 mengirimkan pesan terima kasih kepada client2. Koneksi socket ditutup setelah selesai. Socket digunakan untuk memungkinkan komunikasi dua arah antara client dan server dalam pertukaran data surat.
 
## Output Program 2
```python
python server2.py
```
![socket server2](https://github.com/Zianasti/SISTER_3B/assets/79962655/0ac09df3-b7c6-4f0f-ad3b-1cbd029deb8e)

```python
python client2.py
```
![Socket client2](https://github.com/Zianasti/SISTER_3B/assets/79962655/a53696e0-32cc-450d-b8be-ce9714ae4b50)

# Socket

> Studi Kasus Game: Login Kedalam Game dan Jejak Login yang Tersimpan dalam server

1.	`client.py`

File ini adalah implementasi client socket yang melakukan koneksi ke server socket pada alamat dan port tertentu. Setelah terhubung, client menerima pesan dari server dan mencetaknya. Pesan tersebut berisi waktu saat ini yang dikirim oleh server.

2.	`client2.py`

File ini adalah implementasi client socket lainnya yang melakukan koneksi ke server socket pada alamat dan port tertentu. Client mengirim pesan `"Selamat Datang Prajurit!"` ke server dan menerima data dari server. Data tersebut ditulis ke file `"received.txt"`. Proses ini berlangsung sampai tidak ada data lagi yang diterima.

3.	`server.py`

File ini adalah implementasi server socket yang membuat socket dan mengikatnya ke alamat dan port tertentu. Server mendengarkan koneksi dari client. Setiap kali ada koneksi masuk, server mengirimkan waktu saat ini ke client. Setelah itu, koneksi ditutup.

4.	`server2.py`

File ini adalah implementasi server socket lainnya yang membuat socket dan mengikatnya ke alamat dan port tertentu. Server juga mendengarkan koneksi dari client. Ketika ada koneksi masuk, server menerima pesan dari client, membuka file `"mytext.txt"`, dan mengirimkan isi file tersebut ke client dalam ukuran blok `1024 byte`. Setelah selesai mengirim data, server mengirimkan pesan `"Nuhun sudah login!"` ke client sebelum menutup koneksi.


 Output client 1: 
 ![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/6ebec5bd-20a6-4598-af21-b139e39fb821)
 Output client 2:
 ![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/79aa1938-b678-4b43-9933-b7b2278ad84e)

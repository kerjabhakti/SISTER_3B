# Tema Client Server 1: Order Paket Joki Akun Mobile Legends

File "server.py" berperan sebagai server dalam aplikasi. Fungsinya adalah untuk membuat objek socket menggunakan modul socket, dan mengaitkannya ke alamat host dan port yang telah ditentukan, dan siap menerima koneksi yang masuk. Setiap kali ada koneksi yang masuk, server akan menerima koneksi tersebut dan mencetak informasi mengenai pengguna yang terhubung. Selanjutnya, server akan mengirimkan waktu saat ini kepada klien yang terhubung, kemudian menutup koneksi setelah pengiriman selesai.

Sementara itu, file "client.py" berfungsi sebagai klien dalam aplikasi. Tugasnya adalah untuk membuat objek socket menggunakan modul socket, dan melakukan koneksi ke server dengan menggunakan alamat host dan port yang sama dengan server. Setelah terhubung, klien akan menerima data yang dikirimkan oleh server, yaitu waktu saat order akun, dan mencetak pesan keterangan telah order beserta waktu tersebut. Setelah itu, koneksi akan ditutup.

Secara keseluruhan, file "server.py" dan "client.py" berperan secara terpisah dalam aplikasi ini. Server bertugas menerima koneksi, mencetak informasi pengguna, dan mengirimkan waktu saat ini kepada klien. Sementara itu, klien bertanggung jawab melakukan koneksi ke server, menerima waktu saat ini, dan mencetak pesan keterangan berhasil order joki beserta dengan keterangan waktu order.

## Output Client 1

1. Server 1

![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Socket/SocketServer1.png)

2. Client 1

![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Socket/SocketClient1.png)


# Tema Client Server 2: Proses Joki Akun Mobile Legends

Dalam sistem ini, terdapat dua file, yaitu "server2.py" dan "client2.py", yang saling berinteraksi sebagai server dan klien. Peran utama dari "server2.py" adalah sebagai server, yang bertujuan untuk membuat sebuah objek socket menggunakan modul socket. Objek socket ini akan diikatkan ke alamat host dan port yang telah ditentukan sebelumnya, dan kemudian server akan mendengarkan koneksi yang masuk.

Setiap kali ada koneksi yang terhubung, server akan menerima pesan dari klien yang terhubung tersebut. Selanjutnya, server akan membaca isi dari file "mytext.txt" dan mengirimkannya kembali ke klien melalui koneksi yang aktif. Setelah semua data terkirim, server akan mengirimkan pesan konfirmasi ke klien dan menutup koneksi tersebut.

Di sisi lain, file "client2.py" berfungsi sebagai klien dalam sistem ini. Tugas utama klien adalah untuk membuat objek socket menggunakan modul socket, dan kemudian melakukan koneksi ke server menggunakan alamat host dan port yang sama seperti yang telah ditentukan sebelumnya. Setelah terhubung ke server, klien akan mengirimkan pesan "Order Joki Paket Epic Abadi To Mythic" ke server melalui koneksi yang aktif.

Selanjutnya, klien akan menerima data yang dikirimkan oleh server melalui koneksi tersebut, dan menuliskannya ke dalam file yang bernama "received.txt". Setelah semua data diterima, koneksi antara klien dan server akan ditutup.

Secara keseluruhan, "server2.py" dan "client2.py" bekerja bersama dalam sistem ini. Server bertindak sebagai penerima pesan dari klien, membaca isi dari file, dan mengirimkannya kembali kepada klien. Di sisi lain, klien bertugas menginisiasi koneksi ke server, mengirimkan pesan kepada server, menerima data yang dikirimkan oleh server, dan menuliskannya ke dalam file.

## Ouput Client 2

1. Server 2

![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Socket/SocketServer2.png)


2. Client 2

![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Socket/SocketClient2.png)

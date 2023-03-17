Program tersebut adalah sebuah program untuk mengelola tagihan dengan menggunakan thread dan queue pada Python. Program tersebut terdiri dari dua fungsi utama yaitu fungsi untuk mengisi queue dengan tagihan dan fungsi untuk memproses tagihan.

Ketika program dijalankan, program akan membuat dua thread, satu untuk mengisi queue dan satu lagi untuk memproses tagihan. Setiap thread akan dijalankan secara bersamaan dan akan menampilkan waktu saat thread dimulai dan saat thread selesai dijalankan.

Fungsi isi_queue akan mengisi queue dengan daftar tagihan, sementara fungsi proses_tagihan akan mengambil tagihan dari queue dan memprosesnya. Setelah semua tagihan diproses, program akan menampilkan pesan "Semua tagihan telah diproses" dan waktu saat itu terjadi.

Program tersebut merupakan contoh implementasi multithreading di Python. Secara keseluruhan, program tersebut berfungsi untuk mengisi tagihan pada suatu queue dan memproses tagihan tersebut secara asinkron. Berikut adalah deskripsi tiap baris program tersebut:

1. Mengimport module threading, queue, dan time.
2. Membuat objek Queue.
3. Mendefinisikan fungsi isi_queue() untuk mengisi queue dengan tagihan listrik, air, telepon, dan internet, dan menambahkan pesan print yang menunjukkan kapan thread dimulai dan selesai.
4. Mendefinisikan fungsi proses_tagihan() untuk memproses tagihan pada queue dengan 5 .5. mengambil tagihan dari queue dan menambahkan pesan print yang menunjukkan kapan thread dimulai dan selesai.
5. Membuat dua objek thread t1 dan t2 untuk mengisi queue dan memproses tagihan pada queue.
6. Memulai kedua thread dengan memanggil metode .start() pada t1 dan t2.
7. Menunggu kedua thread selesai dengan memanggil metode .join() pada t1 dan t2.
8. Menambahkan pesan print yang menunjukkan bahwa semua tagihan telah diproses dan menunjukkan waktunya.
![Screenshot output](https://user-images.githubusercontent.com/112412781/225798949-7200c73e-53fc-4fb8-bc37-4fe6ce2fdac4.png)

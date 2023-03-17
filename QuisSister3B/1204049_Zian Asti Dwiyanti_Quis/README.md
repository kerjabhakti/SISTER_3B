# QUIS
## Studi Kasus : Surat Menyurat
Studi kasus pada codingan tersebut adalah simulasi pengiriman surat yang terdiri dari empat tahap, yaitu persiapan data surat, pembuatan surat, pengiriman surat, dan pelaporan hasil pengiriman. Masing-masing tahap dilakukan dalam satu fungsi. 

## Narasi 
File ini bertujuan untuk melakukan pengeksekusian beberapa pekerjaan dalam 1 waktu dengan menggunakan Python dan modul threading serta syncronization.

Pada codingan tersebut, terdapat fungsi-fungsi yang digunakan untuk melakukan persiapan data surat, pembuatan surat, pengiriman surat, dan pelaporan hasil pengiriman. Masing-masing fungsi diberi tambahan kode untuk menampilkan waktu saat fungsi tersebut dimulai dan selesai dieksekusi.

Selanjutnya, terdapat fungsi *run_letter* yang digunakan untuk menjalankan thread untuk setiap surat. Pada fungsi ini, akan dijalankan fungsi-fungsi persiapan data, pembuatan surat, pengiriman surat, dan pelaporan hasil pengiriman, dengan tambahan kode untuk menampilkan waktu saat fungsi tersebut dimulai dan selesai dieksekusi. Selain itu, juga terdapat penggunaan barrier untuk sinkronisasi antar thread.

Pada script utama, dilakukan inisiasi objek thread dengan menggunakan modul threading, dan juga inisiasi lock dan barrier untuk sinkronisasi antar thread. Selanjutnya, dijalankan thread untuk setiap surat dengan menggunakan loop, dan setiap thread akan di-start menggunakan fungsi *start()*. Kemudian, setelah semua thread selesai dijalankan, dilakukan join untuk setiap thread untuk menunggu sampai semua thread selesai dieksekusi.

Seluruh proses ini akan ditampilkan waktu saat dimulai dan selesai dieksekusi dengan format waktu jam:menit:detik.

Sehingga dapat dikatakan bahwa script ini dapat digunakan untuk melakukan pengeksekusian beberapa pekerjaan dalam 1 waktu dengan menggunakan Python dan modul threading serta syncronization, dengan hasil output yang menampilkan waktu saat fungsi tersebut dimulai dan selesai dieksekusi.

## Screenshoot Hasil Program

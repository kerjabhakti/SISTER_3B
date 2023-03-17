# QUIS
## Studi Kasus : jadwal kuliah

## Narasi
studi kasus penggunaan threading pada Python untuk mengatur jadwal kuliah. Dalam kasus ini, terdapat 4 kelas yang akan diadakan pada hari Senin dan Rabu dengan durasi 2 jam setiap kelasnya. Tujuan dari script ini adalah untuk menentukan jadwal waktu yang tepat untuk mengadakan kelas-kelas tersebut.

Script ini menggunakan class Kelas untuk membuat objek kelas yang memiliki atribut nama, hari, dan jam_mulai, serta method jadwal yang mencetak informasi tentang jadwal kelas. Kemudian, script menggunakan thread dan queue untuk menjalankan proses utama. Terdapat satu thread untuk menjalankan setiap objek Kelas. Thread akan terus berjalan selama masih ada objek Kelas yang perlu diproses dalam queue. Thread akan berhenti jika queue sudah kosong dan tidak ada lagi objek Kelas yang perlu diproses.

Untuk menghentikan thread ketika tidak ada lagi objek Kelas yang perlu diproses, script menggunakan sebuah event stop_event yang akan diset ketika queue sudah kosong. Kemudian, event ini akan diteruskan ke dalam thread dengan mengirimnya sebagai parameter stop_event. Saat queue sudah kosong, event akan diset dan thread akan berhenti. Setelah semua thread selesai dijalankan, script akan mencetak pesan bahwa proses pengeksekusian beberapa kelas dalam 1 waktu sudah selesai.


![Gambar](/SISTER_3B/QuisSister3B/1204044_FAHIRA_QUIS/output.png)
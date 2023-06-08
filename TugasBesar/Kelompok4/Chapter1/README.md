##Penjelasan :

- Pertama, kita mengimpor modul multiprocessing untuk mendukung pemrograman paralel.
Fungsi register(username) digunakan untuk melakukan pendaftaran pengguna. Di sini, kita hanya mencetak pesan untuk menunjukkan dimulainya dan berakhirnya proses pendaftaran. Dalam kasus nyata, Anda akan menambahkan logika pendaftaran yang sesuai.
- Fungsi login(username) digunakan untuk proses login pengguna. Seperti pendaftaran, kita hanya mencetak pesan untuk menunjukkan dimulainya dan berakhirnya proses login.
Pada blok utama, kita mendefinisikan daftar nama pengguna yang akan mendaftar dan login.
- Selanjutnya, kita membuat proses-proses untuk setiap pengguna dalam loop pertama. Setiap proses mewakili proses pendaftaran pengguna.
- Kemudian, kita memulai setiap proses pendaftaran dengan menggunakan metode start().
- Setelah semua proses pendaftaran selesai, kita menggunakan join() untuk memastikan bahwa program tidak berlanjut sampai semua proses selesai.
- Setelah proses pendaftaran selesai, kita membuat proses-proses baru untuk setiap pengguna dalam loop kedua. Setiap proses mewakili proses login pengguna.
- Kita memulai setiap proses login dengan menggunakan metode start().
- Terakhir, kita lagi menggunakan join() untuk memastikan bahwa program tidak berlanjut sampai semua proses login selesai.
- Dengan menggunakan modul multiprocessing, kode di atas akan menjalankan proses pendaftaran dan login secara paralel, sehingga mengoptimalkan waktu yang dibutuhkan untuk menyelesaikan kedua tugas tersebut.

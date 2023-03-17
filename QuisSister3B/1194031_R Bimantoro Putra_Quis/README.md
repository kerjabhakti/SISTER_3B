# R Bimantoro Putra - 1194031

## STUDI KASUS : Kemahasiswaan

PENJELASAN

1. Pertama-tama, kita melakukan import modul `threading` dan `time`. Modul `threading` digunakan untuk membuat dan mengelola thread, sedangkan modul `time` digunakan untuk mengukur waktu eksekusi program.
2. Kemudian, kita mendefinisikan variabel global `students` dan `lock`. Variabel `students` berisi dictionary yang berisi nama dan nilai awal skor mahasiswa. Variabel `lock` akan digunakan untuk mengunci (lock) variabel `students` ketika sedang diakses oleh satu thread sehingga tidak bisa diakses oleh thread lain pada saat yang sama.
3. Selanjutnya, kita mendefinisikan fungsi `student_func` yang akan dijalankan oleh setiap thread. Fungsi ini menerima tiga parameter, yaitu `barrier`, `student_name`, dan `score`. `barrier` adalah objek `Barrier` dari modul `threading` yang akan digunakan untuk sinkronisasi antar thread. `student_name` adalah nama mahasiswa yang akan memperoleh skor, sedangkan `score` adalah jumlah skor yang akan diperoleh oleh mahasiswa tersebut.
4. Di dalam fungsi `student_func`, kita menggunakan lock untuk memastikan variabel `students` tidak diakses oleh thread lain pada saat yang sama. Setiap thread akan menambahkan skor yang diperoleh ke variabel `students`, kemudian mencetak nama mahasiswa dan jumlah skor yang diperoleh, serta skor keseluruhan dari semua mahasiswa.
5. Setelah itu, setiap thread akan memanggil perintah `wait()` pada objek `barrier` untuk menunggu thread lain selesai. Ketika semua thread selesai, `barrier` akan melepaskan semua thread secara bersamaan.
6. Di dalam blok utama program, kita mendefinisikan `tasks` yang berisi daftar tugas yang akan dijalankan. Setiap tugas terdiri dari nama mahasiswa dan jumlah skor yang akan diperoleh.
7. Kemudian, kita membuat objek `Barrier` dengan jumlah thread yang sama dengan jumlah tugas.
8. Selanjutnya, kita membuat thread baru untuk setiap tugas menggunakan `for` loop. Setiap thread akan memanggil fungsi `student_func` dengan parameter yang sesuai.
9. Setelah itu, kita menjalankan semua thread secara bersamaan menggunakan `for` loop dan mencatat waktu mulai eksekusi program.
10. Setelah semua thread selesai dijalankan, kita menghitung waktu total eksekusi program dan mencetak skor akhir dari setiap mahasiswa.
11. Tamat

    SEKIAN DAN TERIMA KASIH

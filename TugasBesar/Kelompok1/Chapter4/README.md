### Dalam kode ini, MPI digunakan untuk mengirim data tugas kuliah dari satu proses ke proses lain, mengumpulkan hasil operasi dari semua proses, dan melakukan komunikasi antar proses. Ini adalah contoh sederhana dari penggunaan MPI untuk pemrograman paralel dengan tema pengumpulan tugas. Berikut ini merupakan penjelasan dari kode program

1. Pada bagian awal file melakukan import modul mpi4py yang dibutuhkan, pembuatan objek komunikator untuk mencakup proses yang berjalan, dan inisiasi variabel size untuk menyimpan jumlah proses yang berkomunikasi, dan variabel rank untuk menyimpan peringkat atau urutan proses saat berkomunikasi

2. Pembuatan variabel tugas_kuliah untuk menampung nilai-nilai tugas, lalu mengirimkannya (broadcast) dari proses ke-0 kepada proses lain

3. Pemeriksaan apakah ada tugas yang sesuai dengan rank proses saat ini pada variabel tugas_kuliah, jika ada maka variabel my_tugas bernilai rank tersebut

4. Mengumpulkan hasil proses pada 1 variabel dari my_tugas ke dalam hasil_tugas

5. Jika rank merupakan urutan ke-0, maka program melakukan loop atau iterasi sebanyak ukuran banyak data tugas dan menyimpan tiap index hasil_tugas, lalu mengeceknya apakah value kosong atau tidak, jika tidak, maka tugas tersebut diberikan ke tugas lain.

6. Sebaliknya jika rank bukan urutan ke-0, maka my_tugas akan dicek apakah berisi atau tidak, jika iya, maka program akan melakukan operasi pada tugas pada urutan tersebut.
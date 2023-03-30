Program di atas menggunakan konsep MPI (Message Passing Interface) untuk mengimplementasikan studi kasus nilai ujian. Program terdiri dari dua jenis proses yaitu server dan mahasiswa.

Pada awal program, setiap proses memanggil fungsi MPI.COMM_WORLD untuk membuat communicator baru, dan kemudian memperoleh rank-nya dengan memanggil comm.rank.

Jika rank = 0, maka proses tersebut adalah server. Server akan memperoleh jumlah mahasiswa dari comm.size dan menghasilkan nilai ujian acak untuk setiap mahasiswa dengan menggunakan fungsi random.randint(). Setelah itu, server akan mengirimkan nilai ujian tersebut ke setiap proses mahasiswa dengan menggunakan perulangan for dan fungsi comm.send().

Jika rank != 0, maka proses tersebut adalah mahasiswa. mahasiswa akan menerima nilai ujian dari proses 0 dengan menggunakan fungsi comm.recv() dan menampilkannya dengan print().

Output program akan menampilkan nilai ujian untuk setiap mahasiswa yang diterima dari server.

## Hasil Output :
![Gambar](mpi.png)
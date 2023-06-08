> Studi Kasus: Food Orders 
### File `mpi.py`:

File mpi.py menggunakan library MPI (Message Passing Interface) untuk melakukan komunikasi dan koordinasi antara beberapa proses yang berjalan secara paralel. Pada kode tersebut, terdapat dua jenis proses: proses server (rank 0) dan proses pelanggan (rank selain 0).

Proses server bertanggung jawab untuk mengirimkan informasi makanan kepada setiap proses pelanggan. Pada awalnya, server akan mencetak pesan bahwa pemesanan makanan dimulai. Kemudian, server akan menentukan jumlah pelanggan berdasarkan ukuran komunikator (comm.size). Setelah itu, server akan menentukan daftar makanan beserta harganya, dan mencetak daftar makanan yang tersedia. Selanjutnya, server akan mengirimkan informasi makanan secara acak ke setiap proses pelanggan menggunakan fungsi comm.send().

Sementara itu, proses pelanggan akan menerima informasi makanan dari proses server menggunakan fungsi comm.recv(). Setiap proses pelanggan akan mencetak pesan bahwa mereka menerima informasi makanan beserta detailnya, seperti nama makanan dan harganya.

Output:
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Tubes_Sister/mpi.png)



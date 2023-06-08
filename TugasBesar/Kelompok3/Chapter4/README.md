 **Deskripsi :**

Pada Chapter 4 ini menggunakan MPI (Message Passing Interface) untuk mengimplementasikan pengurangan (reduction) pada data penjualan dari berbagai node dalam sistem tersebar. Pada awalnya, file ini mengimpor modul mpi4py untuk mendukung komunikasi antar node menggunakan MPI.

Kemudian, ada fungsi reduce_sales_data(sales_data) yang menerima data penjualan dari masing-masing node sebagai argumen. Di dalam fungsi ini, kita menggunakan MPI.COMM_WORLD untuk mendapatkan komunikator MPI yang mencakup semua node dalam sistem. Selanjutnya, comm.Get_rank() digunakan untuk mendapatkan peringkat (rank) masing-masing node.

Selanjutnya, kode menghitung total penjualan di setiap node dengan menggunakan sum(sales_data) untuk menjumlahkan data penjualan.

Setelah itu, comm.reduce() digunakan untuk mengurangi total penjualan dari semua node. Dalam contoh ini, op=MPI.SUM digunakan untuk menjalankan operasi pengurangan dengan melakukan penjumlahan. Node dengan peringkat 0 (root) akan menerima hasil pengurangan.

Jika peringkat node adalah 0, maka kode mencetak total penjualan dari semua node menggunakan print().

Di bagian utama kode, terdapat blok if __name__ == '__main__': yang akan dijalankan ketika file dieksekusi langsung. Di dalam blok tersebut, kita mendefinisikan data penjualan dari masing-masing node dalam variabel sales_data. Setelah itu, kita memanggil fungsi reduce_sales_data() dengan memasukkan data penjualan sebagai argumen.

Dalam modul ini, data penjualan dari masing-masing node didefinisikan sebagai [100, 200, 150, 300]. Ketika kode dijalankan, fungsi reduce_sales_data() akan menghitung total penjualan di setiap node, mengurangi total penjualan dari semua node, dan mencetak hasilnya jika node memiliki peringkat 0.
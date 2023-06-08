**Deskripsi :**

Pada Chapter 3 ini menggunakan modul communicating_with_queue untuk mengimplementasikan komunikasi antara proses menggunakan antrian (queue). Studi kasus yang digunakan adalah pencatatan penjualan dan pembaruan inventaris. Pada awalnya, file ini mengimpor modul multiprocessing untuk mendukung proses multipel.

Selanjutnya, terdapat dua fungsi utama: record_sales() dan update_inventory(). Fungsi record_sales() bertanggung jawab untuk mencatat penjualan, sedangkan fungsi update_inventory() untuk memperbarui inventaris. Kedua fungsi ini berjalan dalam proses terpisah.

Antrian (queue) digunakan sebagai saluran komunikasi antara proses. Pada bagian utama kode, sebuah antrian dibuat menggunakan multiprocessing.Queue(). Kemudian, proses pencatatan penjualan dan pembaruan inventaris dibuat menggunakan multiprocessing.Process(). Setiap proses diberikan target fungsi yang sesuai dan argumen berupa antrian.

Setelah itu, beberapa contoh data penjualan dan pembaruan inventaris dimasukkan ke dalam antrian menggunakan metode put(). Data-data ini disimulasikan sebagai daftar yang mencakup produk atau item yang terjual atau diperbarui. Setelah semua data dimasukkan, sinyal 'done' juga dimasukkan ke antrian untuk memberikan tanda bahwa proses telah selesai.

Terakhir, metode join() digunakan untuk menunggu kedua proses selesai. Ini memastikan bahwa program akan berakhir setelah kedua proses selesai melakukan tugasnya.
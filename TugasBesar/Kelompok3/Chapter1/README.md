ungsi get_order(order_queue) adalah fungsi yang berjalan di thread terpisah untuk mendapatkan pesanan dari pelanggan. Fungsi ini secara terus menerus memeriksa apakah ada pesanan baru dalam antrian order_queue. Jika ada, pesanan tersebut diambil dari antrian dan diproses menggunakan fungsi process_order(order). Setelah proses selesai, fungsi ini akan menunggu selama 1 detik sebelum memeriksa antrian lagi.

Fungsi process_order(order) adalah fungsi yang memproses pesanan yang diterima. Dalam contoh ini, hanya ada simulasi waktu pengiriman selama 2 detik sebelum mencetak pesan bahwa pesanan telah selesai diproses.

Fungsi send_order(order_queue, order) adalah fungsi yang digunakan untuk mengirim pesanan ke gudang. Fungsi ini menerima dua argumen, yaitu antrian order_queue dan pesanan order. Pesanan tersebut kemudian dimasukkan ke dalam antrian menggunakan metode put().

Selanjutnya, terdapat fungsi-fungsi untuk membaca dan menulis data penjualan dan inventaris dari file.

Fungsi read_sales_data(filename) digunakan untuk membaca data penjualan dari file. Fungsi ini membuka file dengan nama yang diberikan sebagai argumen filename, kemudian membaca setiap baris data dari file dan mengembalikan daftar data penjualan yang telah dibersihkan dari karakter newline.
Fungsi write_sales_data(filename, sales_data) digunakan untuk menulis data penjualan ke file. Fungsi ini membuka file dengan nama yang diberikan sebagai argumen filename dalam mode menulis, kemudian menulis setiap elemen dalam daftar sales_data ke file dengan menambahkan karakter newline di antara setiap elemen.
Fungsi read_inventory_data(filename) dan write_inventory_data(filename, inventory_data) memiliki fungsi yang serupa dengan fungsi untuk membaca dan menulis data penjualan, tetapi kali ini digunakan untuk membaca dan menulis data inventaris.

Setelah itu, program membuat antrian pesanan order_queue dan menjalankan thread untuk mendapatkan pesanan dengan fungsi get_order. Selanjutnya, beberapa thread dibuat untuk mengirim pesanan dengan menggunakan fungsi send_order. Setiap thread akan mengirim pesanan dengan argumen yang berbeda.

Setelah semua thread pengiriman pesanan selesai, program akan menunggu thread mendapatkan pesanan selesai dengan menggunakan metode join() untuk setiap thread. Setelah itu, program membaca data penjualan dari file dengan menggunakan fungsi read_sales_data, menambahkan data baru ke dalam daftar, dan menulis data penjualan baru tersebut ke file menggunakan fungsi write_sales_data. Hal yang sama dilakukan untuk data inventaris dengan menggunakan fungsi read_inventory_data dan write_inventory_data.

Dengan demikian, kode di atas menggabungkan berbagai fungsi dan proses untuk mengatur antrian pesanan, memproses pesanan, membaca dan menulis data penjualan dan inventaris dari file.
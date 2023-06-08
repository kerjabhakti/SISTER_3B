Kode di atas mengimplementasikan proses transaksi penjualan secara paralel menggunakan RLock dan Semaphore.

Pada awalnya, kita menginisialisasi RLock, yaitu rlock, yang akan digunakan untuk mengontrol akses ke bagian kode yang sensitif terhadap race condition.

Selanjutnya, kita membuat antrian pesanan, yaitu order_queue, dengan menggunakan modul queue dari Python.

Kemudian, kita inisialisasi Semaphore dengan nilai 3, yang artinya hanya 3 pesanan yang dapat diproses secara bersamaan. Semaphore ini akan membatasi jumlah thread yang dapat mengakses blok kode yang diatur oleh semaphore.

Berikutnya, kita mendefinisikan fungsi get_order, yang akan dijalankan oleh thread-thread untuk mendapatkan pesanan dari pelanggan. Di dalam fungsi ini, kita menggunakan RLock untuk memastikan akses yang aman ke antrian pesanan. Jika antrian tidak kosong, pesanan diambil dari antrian dan diproses menggunakan fungsi process_order.

Fungsi process_order adalah fungsi yang memproses pesanan. Di sini, kita menggunakan Semaphore untuk membatasi jumlah pesanan yang diproses secara bersamaan. Sebelum memproses pesanan, thread harus memperoleh izin dari Semaphore. Setelah memperoleh izin, thread akan melakukan simulasi waktu pengiriman selama 2 detik dan mencetak pesan bahwa pesanan telah selesai diproses.

Selanjutnya, kita mendefinisikan fungsi send_order, yang digunakan untuk mengirim pesanan ke antrian. Di dalam fungsi ini, kita juga menggunakan RLock untuk memastikan akses yang aman ke antrian. Pesanan dikirim ke antrian menggunakan metode put().

Setelah itu, kita membuat beberapa thread untuk mendapatkan pesanan (get_order_thread1 dan get_order_thread2) serta mengirim pesanan (send_order_thread1, send_order_thread2, dan send_order_thread3).

Selanjutnya, kita memulai eksekusi thread-thread dengan memanggil metode start() untuk masing-masing thread.

Terakhir, kita menggunakan metode join() untuk menunggu thread-thread selesai. Dengan menggunakan join(), kita memastikan bahwa program tidak berakhir sebelum semua thread selesai dieksekusi.

Dengan menggunakan RLock dan Semaphore, kita dapat mengontrol akses ke antrian pesanan dan membatasi jumlah pesanan yang diproses secara bersamaan, sehingga menjalankan proses transaksi penjualan secara paralel dengan aman.
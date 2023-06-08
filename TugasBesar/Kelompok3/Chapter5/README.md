**Deskripsi :**

Pada Chapter 5 ini menggunakan modul asyncio dan futures untuk mengimplementasikan asynchronous programming. Studi kasus yang digunakan adalah menyimpan data penjualan ke dalam database.

Pertama, kita mendefinisikan sebuah fungsi save_sales_data_to_database(sales_data) yang merupakan tugas yang akan dijalankan secara asynchronous. Fungsi ini menerima parameter sales_data yang berisi data penjualan. Di dalam fungsi ini, kita menggunakan asyncio.sleep(1) untuk mensimulasikan waktu yang diperlukan untuk menyimpan data ke database. Kemudian, kita mencetak pesan bahwa data penjualan telah disimpan ke database.

Selanjutnya, kita mendefinisikan fungsi main() sebagai entry point untuk program. Kita membuat variabel sales_data yang berisi daftar data penjualan. Kita juga membuat sebuah list tasks yang akan menampung semua tugas asynchronous yang akan dijalankan.

Selanjutnya, kita menggunakan loop for untuk mengiterasi setiap data penjualan dalam sales_data. Pada setiap iterasi, kita membuat tugas asynchronous menggunakan asyncio.create_task() dengan memanggil fungsi save_sales_data_to_database() dan memberikan data penjualan sebagai argumen. Tugas tersebut kemudian ditambahkan ke dalam list tasks.

Setelah semua tugas telah dibuat, kita menggunakan asyncio.gather() untuk menjalankan semua tugas secara parallel. Kita menggunakan *tasks untuk melewatkan semua tugas sebagai argumen. Fungsi gather() akan menunggu hingga semua tugas selesai dijalankan sebelum melanjutkan eksekusi program.

Terakhir, kita menjalankan program menggunakan asyncio.run(main()) untuk menjalankan fungsi main() secara asynchronous.

Dengan menggunakan asynchronous programming dan asyncio, kita dapat menjalankan tugas-tugas secara parallel dan meningkatkan efisiensi program, terutama dalam kasus-kasus di mana terdapat operasi yang membutuhkan waktu lama seperti menyimpan data ke database.
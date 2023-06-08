**Deskripsi**

Server:
Pada sisi server, kita menggunakan modul socket untuk membuat socket server. Fungsi process_sale(item, price, quantity) merupakan fungsi yang akan dijalankan pada server dan akan memproses penjualan. Fungsi ini menghitung total harga berdasarkan harga per item dan kuantitasnya. Pada fungsi main(), kita membuat socket server menggunakan socket.socket() dengan alamat server 'localhost' dan port 9000. Kemudian, kita menggunakan bind() untuk mengikat socket ke alamat server dan listen() untuk mendengarkan koneksi masuk.

Selanjutnya, dalam loop while, server akan terus menunggu koneksi dari client menggunakan accept(). Setelah koneksi terhubung, server akan menerima data dari client menggunakan recv(). Data yang diterima kemudian diparsing menjadi item, harga, dan kuantitas penjualan. Selanjutnya, server memproses penjualan menggunakan fungsi process_sale() dengan menggunakan data yang telah diparsing. Hasil penjualan tersebut dikirim kembali ke client menggunakan send().

Pada bagian akhir, koneksi dengan client ditutup menggunakan close().

Client:
Pada sisi client, kita juga menggunakan modul socket untuk membuat socket client. Dalam fungsi main(), kita membuat socket client menggunakan socket.socket() dan terhubung ke alamat server 'localhost' dan port 9000 menggunakan connect().

Dalam loop while, client akan meminta input item, harga, dan kuantitas dari pengguna. Data tersebut dikirim ke server menggunakan send() setelah diencode. Client kemudian menerima hasil penjualan dari server menggunakan recv() dan mencetak total harga penjualan. Setelah itu, pengguna diberi pilihan untuk melanjutkan atau tidak.

Pada akhir program, koneksi dengan server ditutup menggunakan close().

Dengan menggunakan modul socket, server dan client dapat saling terhubung. Server akan menerima permintaan penjualan dari client, memprosesnya, dan mengirimkan hasilnya kembali ke client. Client dapat mengirimkan data penjualan ke server dan menerima total harga penjualan dari server. Koneksi antara server dan client dilakukan melalui socket yang dibuat pada masing-masing sisi.
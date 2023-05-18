## Deskripsi Kode Program Chapter 006

### Nama : Fahira 
### NPM : 1204044

Pada tugas chapter 006 ini terdapat 3 latihan project terkait Celery, Pyro4 dan Socket yang dimana masing masing memiliki studi kasusnya

# Celery
> Studi Kasus E-Library: Menampilkan banyaknya halaman buku yang telah dibaca

1. `addTask_main.py` :
Ini adalah file utama yang mengimpor modul addTask dan menggunakan fungsi `add()` dari modul tersebut. Fungsi `add()` mengambil dua parameter x dan y, dan mengembalikan hasil penjumlahan keduanya. Pada contoh ini, fungsi `add()` dipanggil dengan argumen 4 dan halaman, dan hasilnya disimpan dalam variabel result. Kemudian, hasilnya dicetak menggunakan pernyataan print(). Contoh ini bertujuan untuk menunjukkan penggunaan modul addTask dalam skrip utama.

2. `addTask.py`:
Ini adalah modul yang menggunakan Celery untuk melakukan tugas secara asinkron. Modul ini mendefinisikan objek Celery dengan nama addTask dan menggunakan broker `AMQP (amqp://guest@localhost//)` untuk mengatur komunikasi antara pengirim dan penerima tugas. Terdapat fungsi `add()` yang didekorasi dengan @app.task, yang berarti fungsi ini akan dianggap sebagai tugas Celery yang dapat dipanggil secara asinkron. Fungsi `add()` mengambil dua parameter `x` dan `y`, dan mengembalikan hasil penjumlahan keduanya. Modul ini bertujuan untuk menunjukkan penggunaan Celery dalam membuat dan menjalankan tugas async sederhana.

# Menjalankan Program
  
Sebelum dapat menjalankan aplikasi ini, pastikan Anda telah menginstal Celery, erlang 25.3.2, dan RabbitMQ 3.11.16. Selain itu, jangan lupa untuk menjalankan server RabbitMQ dengan URL yang sesuai seperti yang terkonfigurasi di file "addTask.py".


# Hasil dari program
  
  


# Pyro4
> Studi Kasus E-Library : Membeli buku dan Proses membaca buku

- First Example

1.	`pyro_client.py`:
File ini merupakan client yang menggunakan library Pyro4 untuk berkomunikasi dengan server. Pada awalnya, ada baris yang di-comment dengan `#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()`, yang dapat digunakan untuk memasukkan URI server Pyro4 secara manual. Kemudian, pengguna diminta untuk memasukkan nickname melalui `name = input("Mau beli buku dengan judul apa? ").strip()`. Selanjutnya, client menggunakan proxy Pyro4 untuk menghubungi server menggunakan URI PYRONAME:server. Setelah itu, client mencetak pesan selamat datang yang diterima dari server. Contoh ini bertujuan untuk menunjukkan penggunaan Pyro4 dalam komunikasi antara klien dan server.


2.	`pyro_server.py`:
File `pyro_server.py` adalah file yangg menggunakan library Pyro4 untuk melayani permintaan dari client. Dalam kelas Server, terdapat metode `welcomeMessage()` yang diberi dekorator `@Pyro4.expose`. Metode ini menerima parameter `name` dan mengembalikan pesan selamat datang yang mencakup nilai `name` yang diterima. Pada fungsi `startServer()`, server Pyro4 dibuat menggunakan objek Server dan daemon Pyro4. Daemon tersebut kemudian didaftarkan dengan name server yang telah ditemukan. URI server diambil dengan `daemon.register(server)` dan didaftarkan dalam name server dengan nama "server". URI server kemudian dicetak untuk digunakan oleh client. Terakhir, event loop daemon dimulai dengan `daemon.requestLoop()`. Contoh ini bertujuan untuk menunjukkan penggunaan Pyro4 dalam membuat server Pyro4 yang menerima permintaan dari client. File "pyro_server.py" berperan sebagai server Pyro yang mendefinisikan kelas "Server" dengan metode "welcomeMessage" yang akan dipanggil oleh client. Metode tersebut mengembalikan pesan sambutan yang mencakup judul buku yang diberikan oleh client.


- Second Example

1.	`chainTopology.py`

File ini implementasi kelas `Chain` yang menggunakan Pyro4 untuk komunikasi jarak jauh. Kelas ini memiliki metode `process` yang digunakan untuk memproses pesan. Saat memproses pesan, jika nama buku terdapat dalam pesan, maka akan mencetak pesan "Kembali ke buku [nama buku]" dan mengembalikan pesan tersebut. Jika nama buku tidak terdapat dalam pesan, pesan akan mencetak bahwa buku telah selesai dibaca dan melanjutkan ke buku berikutnya dengan memanggil metode `process` pada server yang ditentukan. Hasilnya akan dimasukkan ke dalam variabel `result` dan pesan akan dikembalikan dengan menambahkan pesan "Buku [nama buku] sudah selesai di baca!". Kode ini memanfaatkan Pyro4 untuk mengatur komunikasi jarak jauh dengan server.

2.	`client_chain.py`

Ini adalah file client yang menggunakan Pyro4 untuk terhubung ke server dengan nama `example.chainTopology.1`. Kemudian, objek `obj` memanggil metode `status` dengan pesan "hello" sebagai argumen, dan mencetak hasilnya.

3.	`server_chain_1.py`

File ini adalah file server yang menggunakan Pyro4 untuk membuat objek Chain dengan nama server `"example.chainTopology.1".` Objek tersebut didaftarkan ke name server dan memulai daemon untuk menerima panggilan.

4.	`server_chain_2.py`

File ini adalah file server yang serupa dengan `server_chain_1.py`, tetapi dengan nama server `"example.chainTopology.2"` dan `next_server` yang berbeda.

5.	`server_chain_3.py`

File ini adalah file server yang serupa dengan `server_chain_1.py`, tetapi dengan nama server `"example.chainTopology.3"` dan next_server yang berbeda.
File-file ini membentuk topologi rantai dengan tiga server yang saling terhubung. Ketika client `(client_chain.py)` mengirim pesan, pesan tersebut akan diproses oleh objek Chain di setiap server dalam urutan yang ditentukan.

# Menjalankan Program
  
Sebelum dapat menjalankan aplikasi ini, dalam folder `Pyro4` kita harus menjalankan perintah `python -m Pyro4.naming` terlebih dahulu untuk menjalankan server Pyro4 nya


# Hasil dari program
 - Output First Example : 

 - Output Second Example :


# Socket

> Studi Kasus E- Library : Proses pinjam meminjam dan Membeli buku
1. `server.py`
File ini merupakan implementasi server socket yang membuat socket dan mengaitkannya dengan alamat dan port spesifik. Server ini akan terus mendengarkan koneksi yang datang dari klien. Setiap kali ada koneksi masuk, server akan mengirimkan waktu saat ini kepada klien. Setelah itu, koneksi akan ditutup. File `server.py` berfungsi sebagai server. Di dalam file ini, kita membuat objek socket menggunakan modul socket, mengaitkannya dengan alamat host dan port tertentu, dan kemudian menerima koneksi yang masuk. Setiap kali ada koneksi masuk, kita menerima koneksi tersebut dan mencetak informasi tentang pengguna yang terhubung. Selanjutnya, kita mengirimkan waktu saat ini kepada klien dan menutup koneksi.

2. `client.py`
File `client.py` adalah implementasi client socket yang melakukan koneksi ke server soket dengan alamat dan port tertentu. Setelah terhubung, klien menerima pesan dari server dan mencetaknya. Pesan tersebut berisi waktu saat ini yang dikirim oleh server. File `client.py` berfungsi sebagai klien. Di dalam file ini, kita membuat objek soket menggunakan modul soket, dan kemudian kita melakukan koneksi ke server menggunakan alamat host dan port yang sama. Setelah terhubung, kita menerima data dari server, yaitu waktu saat ini, dan mencetak pesan sambutan bersama dengan waktu tersebut. Setelah itu, koneksi ditutup.

3.	`server2.py`
File ini merupakan implementasi lain dari server socket yang membuat socket dan mengaitkannya dengan alamat dan port tertentu. Selain itu, server ini juga mendengarkan koneksi dari klien. Saat ada koneksi masuk, server akan menerima pesan dari klien, membuka file `mytext.txt`, dan mengirimkan konten file tersebut ke klien dalam blok ukuran `1024 byte`. Setelah selesai mengirimkan data, server akan mengirim pesan `Peminjaman buku telah selesai diproses` kepada klien sebelum menutup koneksi.

4.	`client2.py`
File ini merupakan implementasi lain dari client socket yang melakukan koneksi ke server socket di alamat dan port tertentu. Client ini mengirimkan pesan `Pinjam Buku Programming GO!` ke server dan menerima data dari server. Data tersebut akan dituliskan ke dalam file `received.txt`.


# Hasil dari program
 - Output client 1: 

 - Output client 2:
 



# Link Youtube Untuk Chapter 006 - Fahira 

[Link Video Youtube]()




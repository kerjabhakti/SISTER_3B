### Dalam kode ini, merupakan contoh penggunaan Pyro4 dalam membuat program dengan tema pengumpulan tugas. Berikut ini penjelasan dari kode program

#### Catatan: Sebelum menjalankan program, jalankan perintah berikut terlebih dahulu untuk menyalakan nameserver-nya
python -m Pyro4.naming

### Pyro Server

#### Program ini adalah implementasi server menggunakan Pyro4, sebuah library Python untuk komunikasi jarak jauh (remote communication). Program tersebut membentuk server yang dapat menerima permintaan dari client dan memberikan pesan sambutan kepada client.

1. Melakukan import modul Pyro4 yang diperlukan

2. Definisi class Server yang berisi fungsi welcomeMessage yang nantinya akan ditampilkan jika ada request kepada server

3. Definisi fungsi startServer() yang berisi kode-kode server

### Pyro Client

#### Program ini menggunakan modul Pyro4 untuk menghubungkan ke server Pyro yang sedang berjalan, dan mencetak pesan yang diterima dari server setelah meminta user memasukan tugas yang akan dikumpulkan
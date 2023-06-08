# Server-Client Pyro4 (Pemberian Tanggapan)

Ini adalah contoh program server dan client menggunakan Pyro4, sebuah modul Python untuk remote object communication (komunikasi objek jarak jauh). Program ini memungkinkan client untuk mengirimkan tanggapan kepada server dan menerima pesan balasan dari server.

# Penjelasan

Program terdiri dari dua file: "server.py" dan "client.py". server.py berisi implementasi server yang mengekspose sebuah metode "welcomeMessage". Metode ini menerima satu parameter name yang merupakan tanggapan dari client. Server akan mengirimkan pesan balasan yang berisi ucapan terima kasih dan harapan selamat menggunakan objek Pyro4.

"client.py" adalah implementasi client yang berinteraksi dengan server. Client akan mengirimkan tanggapan kepada server dan menerima pesan balasan dari server menggunakan objek Pyro4. Pada contoh ini, tanggapan dari client berupa masukan name yang akan dikirimkan ke server melalui metode welcomeMessage. Server akan mengirimkan pesan balasan yang berisi ucapan terima kasih kepada client.

# Menjalankan Program

1. Pastikan Pyro4 telah terinstal di sistem Anda.
2. Unduh atau salin kode program server.py dan client.py.
3. Jalankan terlebih dahulu server dari Pyro4 dengan perintah "python -m Pyro4.naming" hingga menghasilkan output sebagai berikut:

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/e352b6fe-a96e-4124-9f27-6ba8c71f74a6)

5. Jalankan server dengan menjalankan perintah python server.py di terminal atau lingkungan pengembangan Python.
6. Setelah server berjalan, jalankan client dengan menjalankan perintah python client.py di terminal atau lingkungan pengembangan Python.
7. Pada client, masukkan tanggapan Anda saat diminta. Misalnya, Anda dapat memberikan saran dan tanggapan terhadap pelayanan yang diberikan.
8. Client akan mengirimkan tanggapan Anda ke server dan menerima pesan balasan yang berisi ucapan terima kasih dari server.
9. Pesan balasan dari server akan ditampilkan di client.

# Hasil Eksekusi

### Server

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/4f22dd15-bcba-4481-9553-84653d66cfcd)

### Client

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/c9a83fec-813c-4dfa-b0ca-71b5981641e9)

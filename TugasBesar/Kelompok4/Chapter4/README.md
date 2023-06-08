# Pengiriman Mobil

berikut adalah program yang menunjukkan proses pengiriman mobil menggunakan MPI (Message Passing Interface) dengan modul mpi4py di Python. Program ini mensimulasikan pengiriman mobil dari Jakarta hingga akhirnya tiba di Yogyakarta melalui beberapa tempat di Indonesia.
  
# Penjelasan
  
Program ini menggunakan MPI untuk mengorganisir komunikasi antar proses secara paralel. Setiap proses yang ada mewakili sebuah tempat di Indonesia, seperti Jakarta, Surabaya, Bandung, Medan, dan Yogyakarta. Proses Jakarta (proses dengan rank 0) menerima pesanan mobil dan mengirimkan pesanan pertama ke Surabaya (rank 1). Kemudian, proses-proses berikutnya menerima mobil dari proses sebelumnya dan mengirimkannya ke proses berikutnya sesuai urutan tempat.

Pada akhirnya, mobil akan tiba di Yogyakarta (rank 4) dan program akan mencetak pesan bahwa mobil akan dikirimkan ke pemesan. Program ini mensimulasikan proses pengiriman dengan menambahkan jeda waktu (time.sleep) sebagai representasi dari proses pengiriman yang sebenarnya.

# Menjalankan Program 

1. Pastikan MPI dan modul mpi4py telah terinstal di sistem Anda.
2. Unduh atau salin kode program pengiriman_mobil.py.
3. Jalankan program dengan perintah mpiexec -n 9 python pengiriman_mobil.py, di mana <jumlah_proses> adalah jumlah proses yang ingin Anda jalankan (misalnya, 5 proses untuk tempat-tempat yang ada).
5. Anda akan melihat output yang menampilkan informasi pengiriman mobil dari satu tempat ke tempat berikutnya.
6. Pada akhirnya, program akan mencetak pesan bahwa mobil akan dikirimkan ke pemesan setelah tiba di Yogyakarta.

# Hasil Eksekusi

![image](https://github.com/ilmanaqilaa/SISTER_3B/assets/80626628/f099b032-0ac8-4e46-8c4d-42b089220057)

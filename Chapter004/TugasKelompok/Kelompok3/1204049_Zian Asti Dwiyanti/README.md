### 1204049 - Zian Asti Dwiyanti
### Studi Kasus : Surat Menyurat
### Deskripsi :
Pada implementasi penggunaan MPI (Message Passing Interface) dalam Python untuk studi kasus pengiriman surat menyurat diilustrasikan bagaimana MPI dapat digunakan untuk mengirimkan data surat dari satu proses ke proses-proses lain dalam suatu komunikator MPI.

Pada awal kode, modul mpi4py dan numpy diimpor untuk mengakses fungsi-fungsi MPI dan operasi-operasi pada array numerik. Selanjutnya, MPI diinisialisasi dengan membuat objek komunikator MPI, mengambil nomor identifikasi proses saat ini (rank), dan mengambil jumlah total proses yang berjalan (size).

Selanjutnya, data surat yang akan dikirim dipersiapkan di rank 0 dalam bentuk daftar (list) dengan nama surat-surat yang dihasilkan secara statis. Kemudian, data surat tersebut di-broadcast dari rank 0 ke semua proses yang ada dalam komunikator MPI menggunakan fungsi comm.bcast(), yang akan mengirimkan data surat ke seluruh proses dalam komunikator.

Setiap proses, mulai dari rank 0 hingga rank 4, akan mengolah data surat yang telah diterima setelah broadcast dilakukan. Dalam contoh ini, setiap proses hanya akan mencetak pesan yang menunjukkan rank proses dan data surat yang diolah.

Setelah semua proses selesai dieksekusi, komunikasi MPI ditutup menggunakan fungsi MPI.Finalize(). Dengan demikian, kode tersebut memberikan gambaran sederhana tentang bagaimana MPI dapat digunakan dalam konteks pengiriman data surat menyurat antar proses dalam suatu komunikator MPI.

### Output
![chapter4](https://user-images.githubusercontent.com/79962655/230627335-6ae5b375-27e3-48dc-b0bc-9fd9f687971b.jpg)

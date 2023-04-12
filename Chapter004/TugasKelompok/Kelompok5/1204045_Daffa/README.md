## Studi Kasus: Pembagian Tugas

## Penjelasan

Program Python tersebut adalah sebuah contoh implementasi dari pembagian pekerjaan dalam sebuah tim untuk menyelesaikan tugas besar menggunakan MPI (Message Passing Interface) di dalam bahasa pemrograman Python. Berikut adalah penjelasan programnya secara rinci:

- Impor modul MPI dari mpi4py pada baris pertama.
- Inisialisasi komunikator MPI dengan objek COMM_WORLD pada baris kedua, kemudian setel rank dari proses MPI pada variabel 'rank'.
- Kemudian pada baris 8-9 terdapat inisialisasi nama anggota tim dan tugas yang akan dikerjakan.
- Selanjutnya pada baris 10-11, inisialisasi jumlah anggota tim dan jumlah tugas.
- Kemudian pada baris 14-16, bagi tugas ke dalam 8 bagian sesuai dengan jumlah anggota tim menggunakan perulangan.
- Pada baris 19 akan dilakukan pengiriman bagian tugas ke setiap anggota tim menggunakan metode 'send' dari objek komunikator MPI, dengan diakhiri pesan bahwa Pembagian tugas telah dilakukan
- Pada bagian else (baris 23-35), proses akan menerima tugas yang diberikan oleh manajer tim (rank=0).
- Program pada baris 25, akan menerima tugas yang diberikan oleh manajer tim (rank=0) menggunakan metode 'recv' dari objek komunikator MPI.
- Program pada baris 28-29 akan menunjukkan bahwa pekerjaan yang diberikan sedang diproses (dengan mencetak pesan).
- Program pada baris 32-33, akan mengirim hasil pekerjaan ke manajer tim (rank=0) menggunakan metode 'send' dari objek komunikator MPI.
- Program pada baris 35, akan memberi pesan bahwa anggota tim telah selesai mengerjakan tugas.

## Output
![image](https://user-images.githubusercontent.com/112412781/228729804-dc830952-2a77-4853-8fbc-77deecb418a2.png)

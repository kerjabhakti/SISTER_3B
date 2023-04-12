# Studi Kasus: Pesanan Makanan

## Penjelasan program pada file spawning.py(Jawaban nomor 1)

Program ini menggunakan modul multiprocessing untuk memproses daftar pesanan makanan secara paralel. Dalam program ini, terdapat fungsi `process_order()` yang mengambil satu argumen, yaitu order, yang merepresentasikan satu pesanan makanan. Fungsi ini bertanggung jawab untuk memproses pesanan makanan. Didalam blok program pada baris 11, terdapat sebuah daftar orders yang berisi daftar pesanan makanan yang akan diproses. Setiap pesanan dalam daftar ini akan diproses oleh sebuah proses yang dibuat menggunakan modul multiprocessing. Setiap proses akan diproses secara paralel dan akan memanggil fungsi `process_order()` dengan satu pesanan makanan sebagai argumen. Setelah semua proses selesai diproses, program akan menampilkan pesan "Semua pesanan telah diproses".

## Output spawning.py

![Output soal 1](output/Output%20soal%201.png)

## Penjelasan program pada file spawning_time.py(Jawaban nomor 2)

Program ini menggunakan modul multiprocessing pada Python untuk memproses daftar pesanan makanan secara paralel. Setiap pesanan akan diproses dalam sebuah proses yang terpisah dan akan ditampilkan informasi waktu saat memulai dan menyelesaikan proses. Setelah semua proses selesai diproses, program akan menampilkan pesan "Semua pesanan telah diproses" beserta informasi waktu saat program tersebut dijalankan.

## Output spawning_time.py

![Output soal 2](output/Output%20soal%202.png)

## Penjelasan program pada file mpi.py(Jawaban nomor 3)

Program ini menggunakan MPI untuk melakukan pemrosesan paralel. Program ini memiliki beberapa tahapan sebagai berikut:

1. Inisialisasi MPI
   Baris pertama program ini adalah inisialisasi MPI menggunakan modul mpi4py.
2. Mendapatkan rank dan ukuran dari komunikator MPI
   Dalam MPI, setiap proses memiliki rank atau nomor identifikasi. Rank ini digunakan untuk menentukan aliran data pada pemrosesan paralel. Ukuran komunikator MPI menunjukkan jumlah proses yang berpartisipasi dalam pemrosesan paralel.
3. Membagi komunikator MPI menjadi beberapa grup dengan nilai rank yang acak
   Dalam program ini, komunikator MPI dibagi menjadi beberapa grup dengan menggunakan nilai acak. Hal ini dilakukan agar proses-proses dengan rank yang berbeda dapat melakukan tugas yang berbeda-beda.
4. Mendefinisikan daftar pesanan makanan yang mungkin akan diproses
   Program ini memiliki sebuah daftar pesanan makanan yang mungkin akan diproses. Pesanan makanan ini nantinya akan dipilih secara acak oleh proses dengan rank 0.
5. Mengirim data pesanan dari rank 0 ke seluruh rank lainnya menggunakan PTPC (Point-to-Point Communication)
   Data pesanan yang telah dipilih oleh proses dengan rank 0 dikirimkan ke seluruh proses lainnya menggunakan PTPC. Pada program ini, PTPC yang digunakan adalah broadcast.
6. Memproses pesanan di setiap rank
   Setelah menerima data pesanan dari rank 0, setiap proses kemudian memproses pesanan makanan tersebut. Pada program ini, pesanan makanan diproses dengan menunggu selama satu detik menggunakan fungsi time.sleep(). Setelah selesai diproses, proses akan mengirimkan konfirmasi ke seluruh proses lainnya menggunakan allgather.
7. Menerima konfirmasi pemrosesan dari seluruh rank menggunakan allgather
   Setelah pesanan makanan selesai diproses, setiap proses kemudian mengirimkan konfirmasi ke seluruh proses lainnya menggunakan allgather. Dalam MPI, allgather digunakan untuk mengumpulkan data dari seluruh proses yang berpartisipasi dalam pemrosesan paralel.
8. Menampilkan hasil konfirmasi di rank 0
   Setelah semua konfirmasi diterima, program kemudian menampilkan hasil konfirmasi di rank 0. Hal ini dilakukan karena hanya pada rank 0 hasil output program ini akan ditampilkan.

Pada program ini, terdapat 2 jenis collective communication yang digunakan yaitu:

- `newcomm.bcast(pesanan, root=0)`: Broadcast pesanan dari rank 0 ke seluruh rank lainnya.
- `newcomm.allgather(f"Pesanan {pesanan} telah selesai diproses")`: Gather hasil konfirmasi pemrosesan dari seluruh rank dan mengumpulkannya di seluruh rank.

## Output mpi.py

![Output soal 3](output/Output%20soal%203.png)

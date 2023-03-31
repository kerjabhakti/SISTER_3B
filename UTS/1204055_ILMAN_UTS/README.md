# Pengambilan studi kasus pemesanan terhadap penjualan baju

## Program no 1
Program yang dibuat dengan menggunakan multiprocessing untuk menjalankan atau memproses setiap pesanan dalam sebuah proses yang terpisah dengan memanggil fungsi pesan_baju. Proses akan dijalankan dan dikatakan selesai ketika seluruh proses sudah selesai dengan mengguanakan process.join(). 
![image](https://user-images.githubusercontent.com/80626628/229015722-0cd52f44-06f0-44f7-a02c-0d1af23b4b63.png)

## Program no 2
Program yang dibuat dibuat untuk melakukan pemrosesan pesanan dan mengirimkan pesanan baju dengan menggunakan multiprocessing dan time, yang dimana multiprocessing digunakan untuk dapat melakukan ekseskusi secara parallel pada program. Sedangkan tima merupakan fungsi untuk pemberian waktu delay terhadap proses. Dari program yang dibuat terdapat fungsi pesan_baju() dan kirim_baju(), masing-masing dari fungsi akan dijalankan menggunakan  multiprocessing yang dimana setiap proses pesanan yang akan dijadikan proses. Program akan selesai ketika seluruh proses selesai dilakukan.
![image](https://user-images.githubusercontent.com/80626628/229015848-bd74641e-c7d8-4682-9597-21f5ce25e691.png)

## Program no 3
Program yang dibuat merupakan penerapan dari MPI dengan tujuan pembuatan baju dengan jumlah yang sudah ditentukan. Program akan melakukan pembuatan baju dengan jumlah yang sesuai dan diinisialisai sebagai rank 0, data yang sudah dibuat akan dikirim ke seluruh rank dengan menggunakan broadcast. setiap rank akan melakukan proses sesuai dengan data yang sudah dibuat lalu akan mengirim informasi bahwa pembuatan sidah dikonfirmasi ke seluruh rank.
![image](https://user-images.githubusercontent.com/80626628/229015936-9d99ffa3-1a29-4a69-b6f0-e2fe678f4a04.png)

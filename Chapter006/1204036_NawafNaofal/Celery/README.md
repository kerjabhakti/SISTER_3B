# Celery
> Studi Kasus Game: Menampilkan Level Player

**Agar dapat menjalankan file Celery ini diharuskan untuk melakukan install RabbitMQ dan Erlang agar file ini dapat dijalankan.**

1.	`addTask_main.py`:

File ini adalah file utama yang mengimpor modul addTask dan menggunakan fungsi `add()` dari modul tersebut. Fungsi `add()` mengambil dua parameter x dan y, dan mengembalikan hasil penjumlahan keduanya. Pada contoh ini, fungsi `add()` dipanggil dengan argumen 5 dan 8, dan hasilnya disimpan dalam variabel result. Kemudian, hasilnya dicetak dengan menggunakan pernyataan `print()`. Contoh ini bertujuan untuk menunjukkan penggunaan modul `addTask` dalam skrip utama.

2.	`addTask.py`:

File ini merupakan modul yang menggunakan Celery untuk melakukan tugas asinkron. Modul ini mendefinisikan objek Celery dengan nama addTask dan menggunakan broker `AMQP (amqp://guest@localhost//)` untuk mengatur komunikasi antara pengirim dan penerima tugas. Terdapat fungsi `add()` yang didekorasi dengan `@app.task`, yang berarti fungsi ini akan dianggap sebagai tugas Celery yang dapat dipanggil secara asinkron. Fungsi `add()` mengambil dua parameter `x` dan `y`, dan mengembalikan hasil penjumlahan keduanya. Modul ini bertujuan untuk menunjukkan penggunaan Celery dalam membuat dan menjalankan tugas asinkron sederhana.

Output:
![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/a91d3543-2211-4ad6-a895-94b460f08fee)



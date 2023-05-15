# Tema: Sambutan masuk ke dalam Theater

File "addTask_main.py" adalah file utama yang berfungsi untuk menjalankan contoh penggunaan Celery. Di dalamnya, kita mengimpor modul "addTask" yang merupakan file kedua.

File "addTask.py" adalah file yang berisi definisi dan konfigurasi Celery. Di dalamnya, kita mendefinisikan sebuah task "add" yang menjumlahkan dua nilai.

Ketika menjalankan "addTask_main.py", task "add" akan dijalankan dengan menggunakan Celery. Dimana hasil dari penjumlahan "Theater Dream Come True" dan " Ilman" akan dikembalikan sebagai hasil task dan dicetak sebagai pesan "Selamat datang di <hasil>". Sehingga akan menghasilkan kalimat berbunyi "Selamat datang di Theater Dream Come True Ilman".
  
# Menjalankan Program
  
Untuk menjalankan aplikasi ini, pastikan menginstal Celery dan RabbitMQ terlebih dahulu. Selain itu, tidak lupa untuk menjalankan RabbitMQ server pada URL yang sesuai dengan konfigurasi di file "addTask.py".

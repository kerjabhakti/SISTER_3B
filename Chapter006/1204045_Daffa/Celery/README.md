# Studi Kasus: Food Orders

File "addTask_main.py" berperan sebagai file utama yang bertugas untuk mengoperasikan contoh penggunaan Celery. Di dalamnya, kita mengimport modul "addTask" yang merupakan file kedua.

File "addTask.py" berfungsi sebagai wadah untuk mendefinisikan dan mengkonfigurasi Celery. Di dalamnya, kita menentukan sebuah tugas bernama "add" yang bertugas menjumlahkan dua nilai.

Ketika menjalankan "addTask_main.py", tugas "add" akan dijalankan menggunakan Celery. Hasil penjumlahan antara "Pizza" dan "Coke" akan dikembalikan sebagai hasil tugas dan dicetak sebagai pesan "Your orders", diikuti dengan <result>. Ini akan menghasilkan kalimat yang terdengar seperti "Your orders: Pizza dan Coke".

# Menjalankan Program
  
Sebelum menggunakan aplikasi ini, pastikan Anda telah menginstal Celery dan RabbitMQ. Selain itu, jangan lupa untuk menjalankan server RabbitMQ dengan URL yang sesuai yang terkonfigurasi di file "addTask.py".

# Output
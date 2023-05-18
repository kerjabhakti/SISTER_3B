# Celery
## Studi Kasus : Surat
Dengan menggunakan Celery, kita dapat menjalankan tugas "addTask" secara asinkron dan terdistribusi. Ketika kita menjalankan "addTask_main.py", tugas "addTask" akan dikirimkan ke broker Celery untuk diproses oleh pekerja (worker) yang berjalan di latar belakang. Hasil penambahan dari tugas akan dikembalikan dan disimpan dalam variabel "result" untuk digunakan lebih lanjut.

##### Sebelum menjalankan celery maka harus menginstall RabbitMQ dan Erlang terlebih dahulu dan menjalankannya. 

Output :
![Screenshot 2023-05-18 230800](https://github.com/Zianasti/SISTER_3B/assets/79962655/1aff2b7f-b6a8-4c22-b15c-e89e3316e166)

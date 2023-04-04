# Studi Kasus: Game RPG

## Soal Nomor 1 
Program yang dibuat dalam soal nomor 1 merupakan program yang menggunakan module multiprocessing dari Python untuk menjalankan beberapa proses pada game yang berbeda.

Pada baris pertama, kita mengimport module multiprocessing. Kemudian, kita mendefinisikan fungsi `start_game` yang akan dijalankan sebagai proses untuk setiap game yang dimainkan. Fungsi ini akan mencetak pesan yang memberitahu pemain sedang memulai dan menyelesaikan permainan.

Di dalam blok `if __name__ == '__main__':`, kita membuat sebuah dictionary game_players yang berisi daftar pemain untuk setiap game yang ingin dimainkan. Selanjutnya, kita membuat sebuah list processes yang akan menampung semua proses yang dibuat.

Kemudian, kita melakukan nested loop pada dictionary `game_players`, dan membuat sebuah proses baru untuk setiap pemain pada setiap game menggunakan `multiprocessing.Process`. Proses tersebut akan dijalankan pada fungsi `start_game` dengan parameter `game_name` dan `player_name`.

Terakhir, kita memanggil method join pada setiap proses pada list processes, untuk menunggu semua proses selesai dijalankan sebelum program berakhir.

## Output 1

![image](https://user-images.githubusercontent.com/74226869/229014320-64c66792-2a8e-479c-b0a6-977afd50a978.png)


## Soal Nomor 2
Pada Program kedua ini hampir sama dengan program pertama hanya saja output dari program kedua ini berbeda dengan program pertama karena menggunakan `time.ctime()` yang dimana fungsinya untuk menampilkan waktu. dalam program ini terdapat sebuah fungsi `play_game` yang berisi dua statement print dan `time.sleep(3)` untuk menunjukkan bahwa pemain sedang bermain game. Di dalam `if __name__ == '__main__':`, terdapat sebuah dictionary bernama games yang berisi daftar game beserta pemainnya.

Selanjutnya, proses dilakukan dengan menggunakan `multiprocessing.Process.` Proses ini akan berjalan secara paralel, dan setiap proses akan memanggil fungsi `play_game` dengan argumen player_name dan game_name.

Proses tersebut akan disimpan ke dalam sebuah list bernama processes dan akan dijalankan menggunakan `start()`. Setelah itu, untuk menunggu hingga semua proses selesai, dipanggil `join()` pada setiap proses di dalam processes. Terakhir, dicetak pesan bahwa semua pemain telah selesai bermain game.

## Output 2

![image](https://user-images.githubusercontent.com/74226869/229014379-1e3f58cd-e921-4eb8-bf26-2b44a0167f70.png)


## Soal Nomor 3
Pada program ketiga ini di awal programnya, modul mpi4py diimport dan objek komunikator `MPI.COMM_WORLD` dibuat untuk inisialisasi MPI. Selanjutnya, dilakukan penentuan rank dan ukuran (size) dari setiap proses.

Program juga membentuk topologi menggunakan `MPI.Create_cart()` dengan parameter dims yang dihitung menggunakan `MPI.Compute_dims()` dari ukuran proses. Topologi ini akan digunakan pada komunikasi selanjutnya.

Selanjutnya, program mengandung dua fungsi. Fungsi pertama `(get_random_item())` digunakan untuk mengambil item secara acak dari sebuah list yang berisi item-item yang akan diproses. Fungsi kedua `(process_task())` digunakan untuk memproses tugas, yaitu memproses pembuatan item.

Pada bagian selanjutnya, program menggunakan Point-to-Point Communication (PTPC) untuk memilih tugas secara acak di rank 0 dan mengirim ke setiap proses. Jika rank tidak sama dengan 0, maka tugas akan diinisialisasi dengan None. Setelah itu, tugas yang dipilih di rank 0 akan disebar (scatter) ke setiap proses menggunakan `cart_comm.scatter()` yang merupakan komunikasi dalam topologi yang telah dibentuk.

Setelah tugas diterima, setiap proses akan memproses tugas tersebut dengan menggunakan fungsi `process_task()`. Proses ini dilakukan secara paralel oleh setiap proses.

Pada bagian terakhir program, dilakukan Collective Communication untuk mengumpulkan konfirmasi pemrosesan dari seluruh proses dan menampilkannya pada rank 0. Setiap proses akan mengirimkan konfirmasi pemrosesan pada variabel confirmation, yang kemudian dikumpulkan (gather) oleh rank 0 menggunakan `cart_comm.gather()`. Setelah itu, konfirmasi pemrosesan ditampilkan pada rank 0 menggunakan for loop.

Terakhir, setelah program selesai, topologi yang telah dibentuk akan dihapus dari memori menggunakan `cart_comm.Free()`.

## Output 3

![image](https://user-images.githubusercontent.com/74226869/229014449-216a472c-ef72-465e-9b71-583bec0b861f.png)

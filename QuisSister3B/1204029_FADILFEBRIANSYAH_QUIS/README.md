# Sistem Tersebar Studi Kasus Presensi 
## Fadil Febriansyah 1204029
Kode ini adalah contoh implementasi untuk melakukan presensi mahasiswa di kelas SISTER menggunakan threading

Pada kode program ini menggunakan 2 library yaitu threading dan time
- Threading
Threading ini digunakan untuk membuat thread baru untuk setiap mahasiswa dan menjalankannya secara parallel
- Time ini digunakan untuk mencatat waktu awal dan akhir dari program dan digunakan juga untuk menampilkan waktu ketika mahasiswa melakukan presensi.

```
import threading
import time
```

Pada kode dibawah ini digunakan untuk sinkronisasi antar thread.barrir ini juga memungkinkan beberapa thread untuk bekerja secara paraller dan menunggu satu sama lain sampai proses nya selesai dan dilanjutkan ke tahap berikutnya.
 ```
 barrier = threading.Barrier(4)
 ```

Pada kode dibawah ini mendefinisikan kelas yang bernama Presensi. Didalam kelas Presensi ini memiliki 3 fungsi yaitu

- init__()
Fungsi ini adalah konstruktor kelas yang dipanggil saat objek kelas dibuat. fungsi ini juga menginisialisasi atribut absen sebagai sebuah list kosong.
- tambah()
Fungsi ini digunakan untuk menambahkan nama mahasiswa yang ada di dalam kelas sister 3b kedalam list absesn dan menampilkan pesan bahwa mahasiswa tersebut sudah melakukan absensi.
- lihat
Fungsi ini digunakan untuk menampilkan daftar hadir kelas dengan menampilkan setiap nama dan npm yang sudah melakukan absensi.

 ```
class Presensi:
    def __init__(self):
        self.absen = []

    def tambah(self, nama):
        self.absen.append(nama)
        print(f"{nama} sudah melakukan absensi ya gaes")

    def lihat(self):
        print("Daftar hadir kelas SISTER:")
        for nama in self.absen:
            print(f"- {nama}")
presensi = Presensi()
 ```

Pada kode dibawah ini mendefinisikan kelas yang bernama Mahasiswa. Didalam kelas Presensi ini memiliki 2 fungsi yaitu

- init__()
Fungsi ini adalah konstruktor kelas yang dipanggil saat objek kelas dibuat. fungsi ini juga menginisialisasi objek mahasiswa dengan nilai awal nama dan npm.
- presensi()
Fungsi ini digunakan untuk menambahkan objek mahasiswa ke dalam objek presensi dan menampilkan pesan bahwa mahasiswa tersebut sudah melakukan presensi.

 ```
class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def presensi(self):
        presensi.tambah(self.nama)
        print(f"{self.nama} dengan {self.npm} sudah melakukan presensi pada jam {time.ctime(time.time())}")
        # Thread menunggu di barrier
        barrier.wait()
        print(f"{self.nama} dengan {self.npm} sudah menyelesaikan presensinya\n")
 ```

Pada kode dibawah ini mendefinisikan objek mahasiswa dengan masing masing objek memiliki atrubut nama dan npm yang menjelaskan nama dan nomor mahasiswa.

 ```
 mhs1 = Mahasiswa("Ilman", "1204055")
 mhs2 = Mahasiswa("Nawaf", "1204036")
 mhs3 = Mahasiswa("Daffa", "1204045")
 mhs4 = Mahasiswa("Fadil", "1204029")
 ```

Pada kode dibawah ini merupakan blok utama program yang akan dijalankan.Pada kode program ini dilakukan beberapa hal, yaitu:
1. Pencatatan waktu
2. Membuat thread baru untuk setiap mahasiswa
3. Menjalankan thread dengan memanggil fungsi start()
4. Menunggu thread selesai dengan memanggil fungsi join()
5. Pencatatan waktu selesai dengan memanggil time.time()
6. Menampilkan daftar hadir dengan memanggil fungsi lihat()
7. Menampilkan pesan bahwa semua mahasiswa telah menyelesaikan presensi pada waktu tertentu.
8. Menampilkan perbandingan waktu berjalan dan berhenti dengan menghitung selisih antara waktu mulai dan selesai.

 ```
 if __name__ == '__main__':
    # catat waktu mulai
    start_time = time.time()

    # membuat thread baru untuk setiap mahasiswa
    t1 = threading.Thread(target=mhs1.presensi)
    t2 = threading.Thread(target=mhs2.presensi)
    t3 = threading.Thread(target=mhs3.presensi)
    t4 = threading.Thread(target=mhs4.presensi)

    # menjalankan thread
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # menunggu thread selesai
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # catat waktu selesai
    end_time = time.time()

    # menampilkan daftar hadir setelah semua mahasiswa melakukan presensi
    presensi.lihat()

    # menampilkan pesan ketika semua mahasiswa selesai presensi
    print("Semua mahasiswa telah menyelesaikan presensinya pada jam: ", time.ctime(time.time()))

    # menampilkan perbandingan waktu berjalan dan berhenti
    print("Perbandingan data berjalan dan berhenti = ", end_time - start_time)
 ```

Hasil dari program yang sudah di jalankan


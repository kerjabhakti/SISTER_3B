# Penjelasan Codingan
Pada codingan ini, menggunakan `mpi4py` untuk melakukan komunikasi antara beberapa proses yang berjalan pada sebuah sistem. Berikut adalah penjelasan singkat dari setiap bagian pada codingan ini:

1. Import dependency `mpi4py`

```python
from mpi4py import MPI
```
Pada baris ini, kita mengimport MPI dari modul mpi4py.

2. Inisialisasi MPI

```python
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
```
Pada bagian ini, kita melakukan inisialisasi MPI dengan memanggil MPI.COMM_WORLD. rank adalah nomor identifikasi dari proses saat ini, sedangkan size adalah jumlah total proses yang sedang berjalan.

3. Split komunikator MPI menjadi beberapa grup dengan nilai rank yang acak

```python
rand = random.randint(0, 100)
color = rand % 2
newcomm = comm.Split(color, rank)
```
Pada bagian ini, kita membagi komunikator MPI menjadi beberapa grup dengan nilai rank yang acak menggunakan fungsi Split. color digunakan sebagai pemisah antar grup.

4. Kirim data pesanan dari rank 0 ke seluruh rank lainnya
```python
pesanan = None
if newcomm.Get_rank() == 0:
    pesanan = random.choice(daftar_pesanan)

pesanan = newcomm.bcast(pesanan, root=0)
```
Pada bagian ini, kita mengirimkan data pesanan dari proses dengan rank 0 ke seluruh proses yang lain menggunakan fungsi bcast.

5. Proses memproses pesanan di setiap rank
```python
if newcomm.Get_rank() != 0:
    print(f"Proses {newcomm.Get_rank()}: Memproses pesanan {pesanan}")
    time.sleep(1)
    print(f"Proses {newcomm.Get_rank()}: Selesai memproses pesanan {pesanan}")
```
Pada bagian ini, setiap proses yang bukan proses dengan rank 0 akan memproses pesanan yang diterima.

6. Menampilkan hasil konfirmasi di rank 0
Setelah proses pemrosesan pesanan selesai dilakukan di setiap rank, maka dilakukan konfirmasi hasil pemrosesan dari masing-masing rank. Konfirmasi tersebut dikumpulkan dan ditampilkan di rank 0.
```python
konfirmasi = newcomm.allgather(f"Pesanan {pesanan} telah selesai diproses")

if newcomm.Get_rank() == 0:
    for i in range(newcomm.Get_size()):
        print(konfirmasi[i])
```

Pada bagian ini, dilakukan pengumpulan konfirmasi pemrosesan dari masing-masing rank dengan menggunakan fungsi `allgather()` pada objek komunikator `newcomm`. Hasil konfirmasi disimpan dalam variabel konfirmasi.

Setelah itu, pada rank 0, dilakukan perulangan untuk menampilkan hasil konfirmasi dari seluruh rank menggunakan fungsi `print()`. Perulangan dilakukan sebanyak ukuran komunikator newcomm dengan menggunakan fungsi `Get_size()`. Setiap elemen dalam variabel konfirmasi ditampilkan dengan menggunakan indeks i.

# Penjelasan Program
Program ini menggunakan MPI (Message Passing Interface) untuk melakukan pemrosesan paralel pada game dengan cara memerangi monster. Program ini menginisialisasi komunikator MPI dengan menggunakan `MPI.COMM_WORLD`. Kemudian, komunikator tersebut di-split menjadi beberapa grup dengan nilai rank yang acak menggunakan `comm.Split(color, rank)`. Daftar monster yang mungkin akan muncul dalam game telah didefinisikan sebelumnya dengan `daftar_monster = ['Goblin', 'Orc', 'Troll', 'Dragon', 'Demon']`.

Pada rank 0, dipilih monster acak dari daftar monster dengan menggunakan `monster = random.choice(daftar_monster)`, lalu dikirimkan ke seluruh rank menggunakan `newcomm.bcast(monster, root=0)`. Kemudian, setiap rank memerangi monster dengan kekuatan serangan yang acak menggunakan modul random yang telah di import sebelumnya. Jika kekuatan serangan mencapai nilai 50 atau lebih, maka monster berhasil dikalahkan, dan jika kekuatan serangannya kurang dari 50 maka monster gagal dikalahkan.

Kemudian setelah proses pemerangan monster selesai, setiap rank mengirimkan konfirmasi ke seluruh rank menggunakan `newcomm.allgather(f"Proses {newcomm.Get_rank()}: Berhasil memerangi {monster}")`. Hasil konfirmasi akan ditampilkan pada rank 0 menggunakan `if newcomm.Get_rank() == 0` dan `for i in range(newcomm.Get_size()): print(konfirmasi[i])`.

# Output


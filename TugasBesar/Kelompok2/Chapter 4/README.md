# MPI Monster Battle Game

Ini adalah contoh program menggunakan library mpi4py untuk menjalankan sebuah game di mana proses-proses berkomunikasi dan bekerja sama untuk memerangi monster. Setiap proses akan menjadi pemain yang bertarung melawan monster dengan kekuatan serangan yang acak. Program ini menggunakan paradigma pemrograman paralel dengan menggunakan Message Passing Interface (MPI) untuk memungkinkan komunikasi antarproses.

## Instalasi

Pastikan Anda telah menginstal mpi4py dan memiliki MPI runtime yang sesuai di sistem Anda sebelum menjalankan program ini.

## Menjalankan Program

Untuk menjalankan program ini, gunakan perintah berikut:

```
mpiexec -n <jumlah_proses> python <nama_file.py>
```

`<jumlah_proses>` adalah jumlah proses yang akan dijalankan. Dalam contoh ini, jumlah proses adalah 9.

## Penjelasan Kode

```python
from mpi4py import MPI
import random

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
```

Kode di atas mengimport library mpi4py yang diperlukan dan melakukan inisialisasi MPI. `MPI.COMM_WORLD` adalah komunikator global yang merepresentasikan semua proses yang sedang berjalan. `rank` adalah nomor identitas unik dari setiap proses, sedangkan `size` adalah jumlah total proses yang sedang berjalan.

```python
# Split komunikator MPI menjadi beberapa grup dengan nilai rank yang acak
rand = random.randint(0, 100)
color = rand % 2
newcomm = comm.Split(color, rank)
```

Kode di atas membagi komunikator MPI menjadi beberapa grup dengan menggunakan nilai acak dari `rand`. Setiap grup memiliki nilai `color` yang didapatkan dari `rand % 2`. Proses dengan rank yang sama akan menjadi anggota grup yang sama dan komunikasi hanya dapat dilakukan antara anggota grup yang sama.

```python
# Daftar monster yang mungkin akan muncul dalam game
daftar_monster = ['Goblin', 'Orc', 'Troll', 'Dragon', 'Demon']
```

Kode di atas mendefinisikan daftar monster yang mungkin muncul dalam game.

```python
# Data monster yang akan diproses
monster = None
if newcomm.Get_rank() == 0:
    monster = random.choice(daftar_monster)
```

Kode di atas memilih monster secara acak dari daftar monster hanya pada proses dengan rank 0 (proses utama).

```python
# Kirim data monster dari rank 0 ke seluruh rank lainnya
monster = newcomm.bcast(monster, root=0)
```

Kode di atas mengirimkan data monster dari proses dengan rank 0 ke seluruh proses lainnya menggunakan `newcomm.bcast()`. Sehingga setiap proses akan memiliki nilai monster yang sama.

```python
# Proses memerangi monster di setiap rank
if newcomm.Get_rank() != 0:
    print(f"Proses {newcomm.Get_rank()}: Mulai memerangi {monster}")
    power = random.randint(1, 100)
    print(f"Proses {newcomm.Get_rank()}: Serangan dengan kekuatan {power}")
    if power >= 50:
        print(f"Proses {newcomm.Get_rank()}: Berhasil mengalahkan {monster}")


    else:
        print(f"Proses {newcomm.Get_rank()}: Kekuatan tidak cukup, gagal mengalahkan {monster}")
```

Kode di atas memerangi monster di setiap proses dengan menghasilkan kekuatan serangan yang acak menggunakan `random.randint()`. Jika kekuatan serangan mencukupi (lebih besar atau sama dengan 50), proses tersebut berhasil mengalahkan monster. Jika tidak, proses tersebut gagal mengalahkan monster.

```python
# Terima konfirmasi dari seluruh rank
konfirmasi = newcomm.allgather(f"Proses {newcomm.Get_rank()}: Berhasil memerangi {monster}")
```

Kode di atas mengumpulkan konfirmasi dari seluruh proses menggunakan `newcomm.allgather()`. Setiap proses akan mengirim pesan konfirmasi ke seluruh proses lainnya.

```python
# Menampilkan hasil konfirmasi di rank 0
if newcomm.Get_rank() == 0:
    for i in range(newcomm.Get_size()):
        print(konfirmasi[i])
```

Kode di atas menampilkan hasil konfirmasi dari setiap proses pada proses dengan rank 0 (proses utama).

Program ini mengilustrasikan komunikasi dan kerja sama antarproses menggunakan MPI dalam sebuah game di mana setiap proses memerangi monster.

Output:

![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/e505aee8-fa4c-4b16-b552-4377df5d0022)

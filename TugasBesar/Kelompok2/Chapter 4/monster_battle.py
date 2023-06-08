from mpi4py import MPI
import random

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Split komunikator MPI menjadi beberapa grup dengan nilai rank yang acak
rand = random.randint(0, 100)
color = rand % 2
newcomm = comm.Split(color, rank)

# Daftar monster yang mungkin akan muncul dalam game
daftar_monster = ['Goblin', 'Orc', 'Troll', 'Dragon', 'Demon']

# Data monster yang akan diproses
monster = None
if newcomm.Get_rank() == 0:
    monster = random.choice(daftar_monster)

# Kirim data monster dari rank 0 ke seluruh rank lainnya
monster = newcomm.bcast(monster, root=0)

# Proses memerangi monster di setiap rank
if newcomm.Get_rank() != 0:
    print(f"Proses {newcomm.Get_rank()}: Mulai memerangi {monster}")
    power = random.randint(1, 100)
    print(f"Proses {newcomm.Get_rank()}: Serangan dengan kekuatan {power}")
    if power >= 50:
        print(f"Proses {newcomm.Get_rank()}: Berhasil mengalahkan {monster}")
    else:
        print(f"Proses {newcomm.Get_rank()}: Kekuatan tidak cukup, gagal mengalahkan {monster}")

# Terima konfirmasi dari seluruh rank
konfirmasi = newcomm.allgather(f"Proses {newcomm.Get_rank()}: Berhasil memerangi {monster}")

# Menampilkan hasil konfirmasi di rank 0
if newcomm.Get_rank() == 0:
    for i in range(newcomm.Get_size()):
        print(konfirmasi[i])

# gunakan perintah ini untuk menjalankan file nya mpiexec -n 9 python
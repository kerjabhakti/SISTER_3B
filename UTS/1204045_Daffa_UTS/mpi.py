from mpi4py import MPI
import random
import time

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Split komunikator MPI menjadi beberapa grup dengan nilai rank yang acak
rand = random.randint(0, 100)
color = rand % 2
newcomm = comm.Split(color, rank)

# Daftar pesanan makanan yang mungkin akan diproses
daftar_pesanan = ['nasi goreng', 'ayam goreng', 'mie goreng', 'sate', 'rendang']

# Data pesanan yang akan diproses
pesanan = None
if newcomm.Get_rank() == 0:
    pesanan = random.choice(daftar_pesanan)

# Kirim data pesanan dari rank 0 ke seluruh rank lainnya menggunakan PTPC
pesanan = newcomm.bcast(pesanan, root=0)

# Proses memproses pesanan di setiap rank
if newcomm.Get_rank() != 0:
    print(f"Proses {newcomm.Get_rank()}: Memproses pesanan {pesanan}")
    time.sleep(1)
    print(f"Proses {newcomm.Get_rank()}: Selesai memproses pesanan {pesanan}")

# Terima konfirmasi pemrosesan dari seluruh rank menggunakan PTPC
konfirmasi = newcomm.allgather(f"Pesanan {pesanan} telah selesai diproses")

# Menampilkan hasil konfirmasi di rank 0
if newcomm.Get_rank() == 0:
    for i in range(newcomm.Get_size()):
        print(konfirmasi[i])

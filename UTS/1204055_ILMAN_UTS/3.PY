from mpi4py import MPI
import numpy as np

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Data pemesanan baju
if rank == 0:
    pesanan = [
        {'nama': 'Balmond', 'alamat': 'Jl. Cihampelas No. 65', 'ukuran': 'L', 'jumlah': 3},
        {'nama': 'Sueb', 'alamat': 'Jl. Cibogo No. 30', 'ukuran': 'M', 'jumlah': 5},
        {'nama': 'Danda', 'alamat': 'Jl. Pagaden No. 59', 'ukuran': 'S', 'jumlah': 2}
    ]
else:
    pesanan = None

# Kirim data pesanan dari rank 0 ke seluruh rank lainnya
pesanan = comm.bcast(pesanan, root=0)

# Proses pembuatan baju di setiap rank
if rank != 0:
    for data_pesanan in pesanan:
        print(f'Rank {rank}: Memproduksi {data_pesanan["jumlah"]} baju ukuran {data_pesanan["ukuran"]}, dan akan dikirimkan ke alamat {data_pesanan["alamat"]}')

# Terima konfirmasi pembuatan baju dari seluruh rank
konfirmasi = comm.allgather(f'Rank {rank}: Menyelesaikan pembuatan baju, dan akan di kirimkan!')

# Menampilkan hasil konfirmasi di rank 0
if rank == 0:
    for i in range(size):
        print(konfirmasi[i])
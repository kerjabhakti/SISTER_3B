from mpi4py import MPI
import numpy as np

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Data surat yang akan dikirim
data_surat = None

# Set data surat di rank 0
if rank == 0:
    data_surat = ["Surat 1", "Surat 2", "Surat 3", "Surat 4", "Surat 5"]

# Broadcast data surat dari rank 0 ke semua rank
data_surat = comm.bcast(data_surat, root=0)

# Pengolahan data surat di setiap rank setelah broadcast
if rank == 0:
    print("Rank", rank, "mengolah data surat:", data_surat)
elif rank == 1:
    print("Rank", rank, "mengolah data surat:", data_surat)
elif rank == 2:
    print("Rank", rank, "mengolah data surat:", data_surat)
elif rank == 3:
    print("Rank", rank, "mengolah data surat:", data_surat)
elif rank == 4:
    print("Rank", rank, "mengolah data surat:", data_surat)

# Menutup komunikasi MPI
MPI.Finalize()

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    # Proses 0 adalah server yang akan mengirimkan nilai ujian ke setiap proses siswa
    print("Server started")
    num_mahasiswa = comm.size - 1
    nilai = []
    for i in range(num_mahasiswa):
        # Generate nilai acak untuk setiap mahasiswa
        nilai.append(random.randint(0, 100))

    print("Nilai ujian:", nilai)

    # Kirim nilai ujian ke setiap proses mahasiswa
    for i in range(1, comm.size):
        comm.send(nilai[i - 1], dest=i)

else:
    # Proses mahasiswa akan menerima nilai ujian dari proses 0
    nilai = comm.recv(source=0)
    print("Mahasiswa", rank, "menerima nilai ujian:", nilai)

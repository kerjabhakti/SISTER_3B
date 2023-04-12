from mpi4py import MPI

# Inisialisasi MPI
comm = MPI.COMM_WORLD
npm = comm.Get_rank()
size = comm.Get_size()

if npm == 0:
    revisi = {
        1: 'Revisi Judul Laproan',
        2: 'Revisi Bab 1-3 Laporan',
        3: 'Revisi Bab 4-6 Laporan'
    }
    for i in range(1, size):
        if i in revisi:
            comm.send(revisi[i], dest=i)
            print(f"revisi telah dikirimkan kepada mahasiswa dengan rank {i}.")
else:
    revisi = comm.recv(source=0)
    print(f"Mahasiswa dengan npm {npm} menerima tugas {revisi}.")

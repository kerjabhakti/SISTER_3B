from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Inisialisasi data tugas kuliah
tugas_kuliah = {'tugas1': [90, 80, 70, 85, 95],
                'tugas2': [75, 85, 90, 80, 70],
                'tugas3': [60, 70, 75, 80, 90]}

# Kirim data tugas_kuliah dari root=0 ke semua proses
tugas_kuliah = comm.bcast(tugas_kuliah, root=0)

# Setiap proses melakukan operasi pada data tugas_kuliah
my_tugas = None
if 'tugas{}'.format(rank+1) in tugas_kuliah:
    my_tugas = tugas_kuliah['tugas{}'.format(rank+1)]

# Kumpulkan data hasil operasi dari semua proses pada root=0
hasil_tugas = comm.gather(my_tugas, root=0)

if rank == 0:
    print("Rank = %s " % rank + "menerima data tugas kuliah dari proses lain")
    for i in range(1, size):
        value = hasil_tugas[i]
        if value is not None:
            print("Proses %s memberikan data tugas %s dari tugas%d" % (i, value, i+1))
else:
    if my_tugas is not None:
        print('Proses %s melakukan operasi pada data tugas tugas%d' % (rank, rank+1))

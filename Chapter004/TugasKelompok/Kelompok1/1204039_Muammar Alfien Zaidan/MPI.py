from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# inisialisasi data absensi
absen_pegawai = {'pegawai1': [1, 0, 1, 1, 0], 
                 'pegawai2': [1, 1, 1, 1, 1],
                 'pegawai3': [0, 1, 0, 1, 0]}

# kirim data absen_pegawai dari root=0 ke semua proses
absen_pegawai = comm.bcast(absen_pegawai, root=0)

# setiap proses melakukan operasi pada data absen_pegawai
my_absen = None
if 'pegawai{}'.format(rank+1) in absen_pegawai:
    my_absen = absen_pegawai['pegawai{}'.format(rank+1)]

# kumpulkan data hasil operasi dari semua proses pada root=0
hasil_absen = comm.gather(my_absen, root=0)

if rank == 0:
   print ("Rank = %s " %rank + "menerima data absensi dari proses lain")
   for i in range(1,size):
      value = hasil_absen[i]
      if value is not None:
          print("Proses %s memberikan data absensi %s dari pegawai%d"\
                %(i , value , i+1))
else:
    if my_absen is not None:
        print('Proses %s melakukan operasi pada data absen pegawai%d' % (rank, rank+1))

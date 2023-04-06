from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank

def kirim_data(data, dest):
    comm.send(data, dest=dest)
    print("Pengiriman dari proses %d ke proses %d: %s" % (rank, dest, data))

def terima_data(source):
    data = comm.recv(source=source)
    print("Penerimaan oleh proses %d dari proses %d: %s" % (rank, source, data))
    return data

if rank == 0:
    # Proses 0 mengirim data awal
    kirim_data("Cargo A", dest=1)

    # Proses 0 menerima data dari proses terakhir dan menampilkan hasil akhir
    final_data = terima_data(source=4)
    print("Proses %d menerima data terakhir: %s" % (rank, final_data))

elif rank in [1, 2, 3]:
    # Proses 1, 2, dan 3 menerima data dari proses sebelumnya dan mengirimkannya ke proses berikutnya
    source = rank - 1
    data = terima_data(source=source)
    time.sleep(1) # simulasi proses pengiriman
    kirim_data(data, dest=rank+1)

elif rank == 4:
    # Proses terakhir (4) menerima data dari proses sebelumnya dan mengirimkan hasil akhir ke proses 0
    source = rank - 1
    data = terima_data(source=source)
    time.sleep(1) # simulasi proses pengiriman
    kirim_data("Final Destination: " + data, dest=0)

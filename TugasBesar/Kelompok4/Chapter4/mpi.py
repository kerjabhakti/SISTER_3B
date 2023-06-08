from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank

tempat = ["Jakarta", "Surabaya", "Bandung", "Medan", "Yogyakarta"]

def kirim_mobil(mobil, dest):
    comm.send(mobil, dest=dest)
    print("Pengiriman mobil dari %s ke %s: %s" % (tempat[rank], tempat[dest], mobil))

def terima_mobil(source):
    mobil = comm.recv(source=source)
    print("Penerimaan mobil oleh %s dari %s: %s" % (tempat[rank], tempat[source], mobil))
    return mobil

if rank == 0:
    # Proses Jakarta menerima pemesanan mobil dan mengirimkan pesanan pertama ke Surabaya
    pesanan_mobil = "Sedan A"
    kirim_mobil(pesanan_mobil, dest=1)

    # Proses Jakarta menerima mobil yang telah dipesan dari Medan dan menampilkan hasil akhir
    mobil_terkirim = terima_mobil(source=3)
    print("Proses %s menerima mobil terkirim: %s" % (tempat[rank], mobil_terkirim))

elif rank in [1, 2, 3]:
    # Proses Surabaya, Bandung, dan Medan menerima mobil dari proses sebelumnya dan mengirimkannya ke proses berikutnya
    source = rank - 1
    mobil_diterima = terima_mobil(source=source)
    time.sleep(1)  # Simulasi proses pengiriman mobil
    kirim_mobil(mobil_diterima, dest=rank + 1)

elif rank == 4:
    # Proses Yogyakarta menerima mobil dari Medan
    source = rank - 1
    mobil_diterima = terima_mobil(source=source)
    time.sleep(1)  # Simulasi proses pengiriman mobil
    print("Mobil akan dikirimkan ke pemesan!")


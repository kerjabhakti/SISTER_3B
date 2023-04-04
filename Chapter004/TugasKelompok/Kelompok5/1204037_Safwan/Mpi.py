from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    # Proses 0 adalah server yang akan mengirimkan informasi mobil ke setiap proses penyewa
    print("Rental mobil started")
    num_penyewa = comm.size - 1
    mobil = ["Toyota Avanza", "Daihatsu Xenia",
             "Honda Mobilio", "Suzuki Ertiga", "Mitsubishi Xpander"]
    harga = [250000, 245000, 300000, 280000, 350000]

    print("Mobil yang tersedia:")
    for i in range(len(mobil)):
        print(f"{i+1}. {mobil[i]} (Rp {harga[i]}/hari)")

    # Kirim informasi mobil ke setiap proses penyewa
    for i in range(1, comm.size):
        index_mobil = random.randint(0, len(mobil)-1)
        comm.send((mobil[index_mobil], harga[index_mobil]), dest=i)

else:
    # Proses penyewa akan menerima informasi mobil dari proses 0
    mobil, harga = comm.recv(source=0)
    print("Penyewa", rank, "menerima informasi mobil:")
    print(f"- Mobil: {mobil}")
    print(f"- Harga: Rp {harga}/hari")

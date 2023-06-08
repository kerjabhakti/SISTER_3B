from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    # Proses 0 adalah server yang akan mengirimkan informasi makanan ke setiap proses pelanggan
    print("Pemesanan makanan dimulai")
    num_pelanggan = comm.size - 1
    makanan = [
        "Nasi Goreng",
        "Ayam Bakar",
        "Mie Goreng",
        "Sate Ayam",
        "Bakso",
    ]
    harga = [25000, 35000, 20000, 15000, 18000]

    print("Makanan yang tersedia:")
    for i in range(len(makanan)):
        print(f"{i+1}. {makanan[i]} (Rp {harga[i]})")

    # Kirim informasi makanan ke setiap proses pelanggan
    for i in range(1, comm.size):
        index_makanan = random.randint(0, len(makanan) - 1)
        comm.send((makanan[index_makanan], harga[index_makanan]), dest=i)

else:
    # Proses pelanggan akan menerima informasi makanan dari proses 0
    makanan, harga = comm.recv(source=0)
    print("Pelanggan", rank, "menerima informasi makanan:")
    print(f"- Makanan: {makanan}")
    print(f"- Harga: Rp {harga}")

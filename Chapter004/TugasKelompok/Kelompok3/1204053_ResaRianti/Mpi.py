from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# inisialisasi data
menu = ["Nasi Goreng", "Sate Ayam", "Sop Buntut", "Gado-gado", "Mie Ayam"]
peserta = ["Agus", "Budi", "Citra", "Dewi", "Eka"]
nilai = {}

# simulasi penilaian menu makanan
for i in range(len(menu)):
    if rank == 0:
        print(f"Menu yang akan dinilai: {menu[i]}")
    time.sleep(1)

    for j in range(len(peserta)):
        if j % size == rank:
            skor = round((i+1) * 3.5 + j * 2.1, 2)
            if rank == 0:
                print(f"Peserta {peserta[j]} memberikan nilai {skor}")
                nilai[f"{menu[i]}_{peserta[j]}"] = skor

    time.sleep(1)

# pengumpulan hasil dari setiap proses
hasil = comm.gather(nilai, root=0)

# menampilkan hasil akhir
if rank == 0:
    print("\nHasil penilaian:")
    for data in hasil:
        for key, value in data.items():
            print(f"{key}: {value}")

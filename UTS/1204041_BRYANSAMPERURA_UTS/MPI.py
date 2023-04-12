from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Point-to-Point Communication
if rank == 0:
    for i in range(1, size):
        print(f"Mahasiwa mengecek: Mahasiswa {i}, Mendaptkan nilai.")
        data = comm.recv(source=i)
        print(f"Program: Terima kasih {i} sudah mengecek.{data}")


else:
    print(f"Mahasiswa {rank}: Saya mengecek nilai.")
    data = {'progress': 'Sudah selesai mengecek nilai'}
    comm.send(data, dest=0)

# Collective Communication
data = rank + 1
sum = comm.allreduce(data, op=MPI.SUM)
print(f"Process {rank}: sum of all ranks is {sum}")

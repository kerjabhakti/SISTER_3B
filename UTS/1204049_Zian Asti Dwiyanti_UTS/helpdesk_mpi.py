from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Jumlah request yang harus ditangani oleh setiap agen
requests = np.array([50, 30, 20, 10])

# Mengumpulkan jumlah request dari setiap agen
request_counts = np.empty(size, dtype='i')
comm.Allgather([requests[rank], MPI.INT], [request_counts, MPI.INT])

# Menentukan tugas untuk setiap agen
total_requests = sum(requests)
requests_per_agent = total_requests // size
extra_requests = total_requests % size

if rank < extra_requests:
    my_requests = requests_per_agent + 1
else:
    my_requests = requests_per_agent

# Memeriksa tugas masing-masing agen
print(f"Process {rank}: handling {my_requests} requests")

# Mengirimkan tugas ke agen-agen yang lain
if rank == 0:
    for i in range(1, size):
        comm.send(my_requests, dest=i)
else:
    my_requests = comm.recv(source=0)

# Menyelesaikan tugas
for i in range(my_requests):
    print(f"Process {rank}: handling request {i+1} of {my_requests}")

# Menunggu semua proses selesai
comm.Barrier()
if rank == 0:
    print("All requests handled")

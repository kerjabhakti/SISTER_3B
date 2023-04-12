from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Inisialisasi topologi 
dims = MPI.Compute_dims(size, 2)
cart_comm = comm.Create_cart(dims, periods=[False, False], reorder=False)
coords = cart_comm.Get_coords(rank)

def get_random_item():
    items = ["Health Potion", "Strength Potion", "Defense Potion", "Stamina Potion"]
    return random.choice(items)

def process_task(task):
    print(f"Proses {rank}: Memproses pembuatan {task}")
    time.sleep(1)
    print(f"Proses {rank}: Selesai memproses pembuatan {task}")

# PTPC: Memilih tugas secara acak di rank 0 dan mengirim ke setiap proses
if rank == 0:
    tasks = [get_random_item() for _ in range(size)]
else:
    tasks = None
task = cart_comm.scatter(tasks, root=0)

process_task(task)

# Collective Communication: Mengumpulkan konfirmasi pemrosesan dari seluruh proses dan menampilkannya pada rank 0
confirmation = f"Pembuatan {task} telah selesai diproses pada proses {coords}"
confirmations = cart_comm.gather(confirmation, root=0)
if rank == 0:
    for c in confirmations:
        print(c)
cart_comm.Free()

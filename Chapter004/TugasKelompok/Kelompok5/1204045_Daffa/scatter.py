from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

# Simulasi pembagian pekerjaan dalam sebuah tim untuk menyelesaikan tugas besar
if rank == 0:
    team_members = ["John", "Jane", "Bob", "Alice", "Mark", "Sara", "Tom", "Lisa"]
    tasks = ["Task A", "Task B", "Task C", "Task D", "Task E", "Task F", "Task G", "Task H"]
    team_size = len(team_members)
    task_size = len(tasks)

    # Bagi pekerjaan ke dalam 8 bagian sesuai jumlah anggota tim
    for i in range(team_size):
        task_start = i * task_size // team_size
        task_end = (i + 1) * task_size // team_size

        # Kirim bagian tugas ke anggota tim
        comm.send(tasks[task_start:task_end], dest=i+1)

    print("Pembagian tugas telah dilakukan")

else:
    # Terima tugas yang diberikan oleh manajer tim (rank=0)
    tasks = comm.recv(source=0)

    # Lakukan pekerjaan yang diberikan
    for task in tasks:
        print(f"Anggota tim {rank} sedang mengerjakan {task}")

    # Kirim hasil pekerjaan ke manajer tim
    result = f"Hasil pekerjaan {rank}"
    comm.send(result, dest=0)

    print(f"Anggota tim {rank} telah selesai mengerjakan tugas")

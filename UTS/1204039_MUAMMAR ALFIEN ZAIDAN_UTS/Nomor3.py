from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # Ujang pengen main ayunan
    data = "Aku pengen main ayunan euy"
    comm.send(data, dest=1)
    print("Ujang kirim chat ke Encep")
elif rank == 1:
    # Encep dapet chat sama ngebales
    data = comm.recv(source=0)
    print("Encep dapet chat Ujang")
    print("Ujang ngechat:", data)
    print("Encep ngechat: Sok pake aja..")
    comm.send("Okay, makasihh!", dest=0)
    print("Encep kirim chat ke Ujang")
elif rank == 2:
    # Ryan gak suka main sama anak lain
    print("Ryan main di serodotan karena engga mau main sama anak lain")

comm.barrier()

if rank == 0:
    # Ujang dibolehin main ayunan
    data = comm.recv(source=1)
    print("Ujang dapet chat dari Encep")
    print("Ujang ngechat:", data)

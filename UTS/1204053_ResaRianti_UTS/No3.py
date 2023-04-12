from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Set up topology
dims = MPI.Compute_dims(size, 2)
cart_comm = comm.Create_cart(dims)

# Simulate customer depositing money at a teller
if rank == 0:
    deposit_amount = 100
    print(f"Teller {rank} received a deposit of {deposit_amount} from a customer.")
    # Send deposit amount to adjacent tellers
    right_teller = cart_comm.Shift(0, 1)[1]
    comm.send(deposit_amount, dest=right_teller)
elif rank == size-1:
    # Receive deposit amount from adjacent tellers
    left_teller = cart_comm.Shift(0, -1)[1]
    deposit_amount = comm.recv(source=left_teller)
    print(f"Teller {rank} received a deposit of {deposit_amount} from a customer.")
else:
    # Receive deposit amount from adjacent tellers
    left_teller = cart_comm.Shift(0, -1)[1]
    deposit_amount = comm.recv(source=left_teller)
    print(f"Teller {rank} received a deposit of {deposit_amount} from a customer.")
    # Send deposit amount to adjacent tellers
    right_teller = cart_comm.Shift(0, 1)[1]
    comm.send(deposit_amount, dest=right_teller)

# Gather deposit amounts from all tellers
deposit_amounts = comm.gather(deposit_amount, root=0)

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("Saya adalah pengendara dengan urutan ke %i" % rank)

if rank == 1:
    data_send = "Permintaan perjalanan"
    destination_process = 5
    source_process = 5

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print("Mengirim permintaan %s " % data_send + \
           "ke pengendara %d" % destination_process)
    print("Permintaan berhasil diterima, status: %s" % data_received)

if rank == 5:
    data_send = "Sedang menuju lokasi penjemputan"
    destination_process = 1
    source_process = 1

    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    print("Mengirim status %s " % data_send + \
           "ke pengendara %d" % destination_process)
    print("Status perjalanan dari pengendara %d: %s" % (source_process, data_received))

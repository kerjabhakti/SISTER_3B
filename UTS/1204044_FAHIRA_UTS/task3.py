from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    nama = input('Masukkan nama yang diundang: ')
    email = input('Masukkan alamat email: ')
    tanggal = input('Masukkan tanggal rapat: ')
    tempat = input('Masukkan tempat rapat: ')

    data = [nama, email, tanggal, tempat]
    comm.send(data, dest=1)
    print(f'Data {data} telah dikirim dari rank 0')

elif rank == 1:
    data = comm.recv(source=0)
    nama, email, tanggal, tempat = data
    print(f'Data {data} telah diterima di rank 1')
    print(f'Nama yang diundang: {nama}')
    print(f'Alamat email: {email}')
    print(f'Tanggal rapat: {tanggal}')
    print(f'Tempat rapat: {tempat}')

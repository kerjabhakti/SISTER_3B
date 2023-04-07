from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    print("Selamat datang di sistem registrasi pasien!")
    nama = input("Silakan masukkan nama lengkap Anda: ")
    umur = input("Silakan masukkan umur Anda: ")
    alamat = input("Silakan masukkan alamat lengkap Anda: ")
    
    data_send = {
        "nama": nama,
        "umur": umur,
        "alamat": alamat
    }
    
    destination_process = 1
    comm.send(data_send, dest=destination_process)
    print(f"Data pasien {nama} telah terdaftar!")
    
if rank == 1:
    source_process = 0
    data_received = comm.recv(source=source_process)
    
    print("Sedang memproses data pasien...")
    print(f"Nama: {data_received['nama']}")
    print(f"Umur: {data_received['umur']}")
    print(f"Alamat: {data_received['alamat']}")
    
    data_send = "Data pasien telah diproses"
    destination_process = 0
    comm.send(data_send, dest=destination_process)
    print("Data pasien telah diproses!")
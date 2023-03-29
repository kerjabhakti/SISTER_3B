# Tugas Pertemuan ke 6

* Silahkan buat folder Kelompok (KM)
* Dalam Folder kelompok buat Folder masing-masing anggota (NPM_Nama)
* Kerjakan masing-masing Mahasiswa 1 FIle MPI
* jalankan dan deskripsikan pada README.md nya
* Deskripsi (I File MPI dan Readme.md)

```python
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank = comm.rank
print("saya sekarang urutan ke %i" % (rank))
if rank==1:
data_send= "a"
destination_process = 5
source_process = 5
    data_received=comm.recv(source=source_process)
    comm.send(data_send,dest=destination_process)
    print ("sending data %s " %data_send + \
           "to process %d" %destination_process)
    print ("data received is = %s" %data_received)
if rank==5:
data_send= "b"
destination_process = 1
source_process = 1
    comm.send(data_send,dest=destination_process)
    data_received=comm.recv(source=source_process)
    print ("sending data %s :" %data_send + \
           "to process %d" %destination_process)
    print ("data received is = %s" %data_received)
```

#Keterangan Tugas
Buat Readmenya dan screenshoot hasilnya
Deskripsikan dengan lengkap

## Kriteria penilaian
* Studi Kasus berbeda (Bobot 20)
* Penjelasan pada Readme.md Jelas (bobot 40)
* Script code sesuai stdi kasusnya (Proyek dll) (bobot 40)
* Jika ada kesamaan studi kasus (Semua nilai Hangus)

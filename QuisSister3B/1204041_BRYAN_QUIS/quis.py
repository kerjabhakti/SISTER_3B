import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(4)

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def cek_lulus(self):
        print(f"{self.nama} sedang mengecek hasil studi pada {time.ctime(time.time())}")
        time.sleep(2)
        if self.nilai >= 70:
            print(f"{self.nama} telah lulus dengan nilai {self.nilai}")
        else:
            print(f"{self.nama} tidak lulus dengan nilai {self.nilai}")
        # Thread menunggu di barier
        barrier.wait()
        print(f"{self.nama} selesai mengecek hasil studi\n")

# Data mahasiswa
mahasiswa1 = Mahasiswa("Alfien", 80)
mahasiswa2 = Mahasiswa("Sapwan", 65)
mahasiswa3 = Mahasiswa("Julia", 90)
mahasiswa4 = Mahasiswa("Kiki", 55)

if __name__ == '__main__':
    # membuat thread baru untuk setiap mahasiswa
    t1 = threading.Thread(target=mahasiswa1.cek_lulus)
    t1.start()

    t2 = threading.Thread(target=mahasiswa2.cek_lulus)
    t2.start()

    t3 = threading.Thread(target=mahasiswa3.cek_lulus)
    t3.start()

    t4 = threading.Thread(target=mahasiswa4.cek_lulus)
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # menampilkan pesan ketika semua mahasiswa telah selesai mengecek hasil studi
    print("Semua mahasiswa telah selesai mengecek hasil studi pada jam: ", time.ctime(time.time()))

    start_time = time.time()
    # menentukan daftar mahasiswa yang lulus
    daftar_lulus = [mahasiswa for mahasiswa in [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4] if mahasiswa.nilai >= 70]
    print("Daftar mahasiswa yang lulus:")
    for mahasiswa in daftar_lulus:
        print(f"{mahasiswa.nama} dengan nilai {mahasiswa.nilai}")
    end_time = time.time()
    print("Waktu yang dibutuhkan untuk menentukan daftar mahasiswa yang lulus = ", end_time - start_time)



# Yang ini sudah studi kasusnya sudah diambil Ilman
# import threading
# import time

# # Membuat objek Barrier dengan jumlah thread yang akan dijalankan
# barrier = threading.Barrier(9)

# print("Data Hasil Studi Mahasiswa : \n")
# class Mahasiswa:
#     def __init__(self, mhs, nilai):
#         self.mhs = mhs
#         self.nilai = nilai

#     def ujian(self):
#         print(
#             f"{self.mhs} mulai ujian pada :{time.ctime(time.time())}")
#         time.sleep(2)
        
        
#         print(
#             f"{self.mhs} selesai ujian dengan nilai :{self.nilai} pada {time.ctime(time.time())}")
        
#         # Thread menunggu di barrier
#         barrier.wait()
# # Data Mahasiswa
# mhs1 = Mahasiswa("Alfien", 80)
# mhs2 = Mahasiswa("Agatha", 70)
# mhs3 = Mahasiswa("Bryan", 90)
# mhs4 = Mahasiswa("Jeniffer", 85)
# mhs5 = Mahasiswa("Fadil", 92)
# mhs6 = Mahasiswa("Azizi", 72)
# mhs7 = Mahasiswa("Wan Randal", 89)
# mhs8 = Mahasiswa("Mike", 83)
# mhs9 = Mahasiswa("Carl Doja", 92)

# if __name__ == '__main__':
#     # membuat thread baru untuk setiap Mahasiswa
#     t1 = threading.Thread(target=mhs1.ujian)
#     t1.start()

#     t2 = threading.Thread(target=mhs2.ujian)
#     t2.start()

#     t3 = threading.Thread(target=mhs3.ujian)
#     t3.start()

#     t4 = threading.Thread(target=mhs4.ujian)
#     t4.start()
    
#     t5 = threading.Thread(target=mhs5.ujian)
#     t5.start()

#     t6 = threading.Thread(target=mhs6.ujian)
#     t6.start()

#     t7 = threading.Thread(target=mhs7.ujian)
#     t7.start()
    
#     t8 = threading.Thread(target=mhs8.ujian)
#     t8.start()

#     t9 = threading.Thread(target=mhs9.ujian)
#     t9.start()

#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     t5.join()
#     t6.join()
#     t7.join()
#     # menampilkan pesan ketika semua Mahamhs selesai ujian
#     print("Semua Mahasiswa Mengumpulkan ujian pada Hari dan Jam:\n ", time.ctime(time.time()))

#     # menghitung rata-rata nilai Mahamhs
#     rata2_nilai = (mhs1.nilai + mhs2.nilai + mhs3.nilai + mhs4.nilai + mhs5.nilai
#                    + mhs6.nilai + mhs7.nilai + mhs8.nilai + mhs9.nilai) / 9
#     print("\nRata-rata nilai Mahasiswa = \n", rata2_nilai)

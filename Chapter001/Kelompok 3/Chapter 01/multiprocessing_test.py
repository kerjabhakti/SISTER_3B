# program ini mengimplementasikan multiprocessing python 
# untuk memproses sebuah fungsi yang didefinisikan di file "do_something.py"

#import semua fungsi yang didefinisikan dalam file "do_something.py"
from do_something import *
import time
import multiprocessing

# program akan memulai menghitung waktu mulai dan mendefinisikan jumlah elemen list yang akan 
# dihasilkan dan jumlah proses yang akan dibuat. 
# Selanjutnya, program membuat sebuah list kosong untuk menampung hasil pengolahan fungsi yang akan diproses nantinya.
if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    procs = 10   
    jobs = []

# program akan membuat sebanyak "procs" proses yang masing-masing menjalankan fungsi "do_something" 
# dengan jumlah elemen list "size" dan menempatkan hasilnya ke dalam list kosong yang sudah dibuat sebelumnya. 
# Kemudian, setiap proses dimasukkan ke dalam list "jobs"
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

#  program menjalankan setiap proses pada list "jobs"
    for j in jobs:
        j.start()

# program menunggu setiap proses selesai dijalankan menggunakan metode "join()"
    for j in jobs:
        j.join()

# program menampilkan pesan "List processing complete" dan menghitung waktu eksekusi program sejak awal
    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
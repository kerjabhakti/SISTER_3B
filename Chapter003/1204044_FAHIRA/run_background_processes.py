import multiprocessing
import time

def pay(harga, pembayaran):
    name = multiprocessing.current_process().name
    print ("Memulai %s \n" %name)
    
    if pembayaran >= harga:
        change = pembayaran - harga
        print("pembayaran Sukses! Uang kembalian kamu adalah:", change)
    else:
        print("pembayaran Gagal! Uang kamu tidak cukup.")
    
    print ("Exiting %s \n" %name)

if __name__ == '__main__':
    item_harga = 15000
    jumlah_pembayaran = 10000
    
    pembayaran_process = multiprocessing.Process(name='pembayaran_process', target=pay, args=(item_harga, jumlah_pembayaran))
    pembayaran_process.daemon = True

    NO_pembayaran_process = multiprocessing.Process(name='pembayaran_process', target=pay, args=(item_harga, jumlah_pembayaran))
    NO_pembayaran_process.daemon = False

    pembayaran_process.start()
    NO_pembayaran_process.start()

    pembayaran_process.join()
    NO_pembayaran_process.join()


# Hasilnya sebagai berikut :
# Memulai pembayaran_process 
# pembayaran Gagal! Uang kamu tidak cukup.
# Exiting pembayaran_process

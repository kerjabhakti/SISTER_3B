import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue, nama_pelanggan, pesanan):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.nama_pelanggan = nama_pelanggan
        self.pesanan = pesanan

    def run(self) :
        for item in self.pesanan:
            self.queue.put((self.nama_pelanggan, item))
            print("Pesanan dari", self.nama_pelanggan, "ditambahkan ke antrian.")
            time.sleep(1)
            print("Jumlah pesanan di antrian:", self.queue.qsize())


class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        total_tagihan = 0
        while True:
            if (self.queue.empty()):
                print("Tidak ada pesanan yang harus diolah.")
                break
            else:
                nama_pelanggan, pesanan = self.queue.get()
                harga_pesanan = daftar_menu[pesanan]
                print("Pesanan dari", nama_pelanggan, "dihitung. Harga:", harga_pesanan)
                total_tagihan += harga_pesanan
                time.sleep(1)
        
        print("Total tagihan:", total_tagihan)

if __name__ == '__main__':
    daftar_menu = {"nasi goreng": 10000, "ayam goreng": 12000, "es teh": 3000, "es jeruk": 4000}
    queue = multiprocessing.Queue()
    
    # Proses untuk menerima pesanan
    pesanan_pelanggan_1 = ["nasi goreng", "ayam goreng", "es jeruk"]
    pesanan_pelanggan_2 = ["nasi goreng", "ayam goreng", "es teh", "es jeruk"]
    
    process_producer_1 = producer(queue, "Pelanggan 1", pesanan_pelanggan_1)
    process_producer_2 = producer(queue, "Pelanggan 2", pesanan_pelanggan_2)
    
    # Proses untuk menghitung tagihan
    process_consumer = consumer(queue)
    
    # Mulai semua proses
    process_producer_1.start()
    process_producer_2.start()
    process_consumer.start()
    
    # Tunggu semua proses selesai
    process_producer_1.join()
    process_producer_2.join()
    process_consumer.join()

# Hasilnya sebagai berikut :
# Tidak ada pesanan yang harus diolah.
# Total tagihan: 0
# Pesanan dari Pelanggan 1 ditambahkan ke antrian.
# Pesanan dari Pelanggan 2 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 2
# Pesanan dari Pelanggan 1 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 3
# Pesanan dari Pelanggan 2 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 4
# Pesanan dari Pelanggan 1 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 5
# Pesanan dari Pelanggan 2 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 6
# Jumlah pesanan di antrian: 6
# Pesanan dari Pelanggan 2 ditambahkan ke antrian.
# Jumlah pesanan di antrian: 7


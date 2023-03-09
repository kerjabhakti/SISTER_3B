import multiprocessing

class PembayaranProcess(multiprocessing.Process):
    def __init__(self, total_harga, metode_pembayaran):
        super().__init__()
        self.total_harga = total_harga
        self.metode_pembayaran = metode_pembayaran
    
    def run(self):
        print(f"Total harga yang harus dibayarkan: {self.total_harga}")
        print(f"Metode pembayaran yang dipilih: {self.metode_pembayaran}")
        print("Melakukan proses pembayaran...")
        # Implementasi proses pembayaran di sini
        print("Pembayaran selesai.")
        return

if __name__ == '__main__':
    total_harga = 500000
    metode_pembayaran = "OVO"
    process = PembayaranProcess(total_harga, metode_pembayaran)
    process.start()
    process.join()

# Hasilnya sebagai berikut :
# Total harga yang harus dibayarkan: 500000
# Metode pembayaran yang dipilih: OVO
# Melakukan proses pembayaran...
# Pembayaran selesai. 
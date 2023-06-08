class Pesanan:
    total_pesanan = 0

    def __init__(self, nama_makanan, jumlah_pesanan):
        self.nama_makanan = nama_makanan
        self.jumlah_pesanan = jumlah_pesanan
        Pesanan.total_pesanan += jumlah_pesanan

    def get_info(self):
        return f"Pesanan: {self.nama_makanan}\nJumlah: {self.jumlah_pesanan}"

    def get_total_pesanan(self):
        return f"Total Pesanan: {Pesanan.total_pesanan}"


# Pemesanan Makanan
pesanan_1 = Pesanan("Burger", 2)
print(pesanan_1.get_info())
print(pesanan_1.get_total_pesanan())

pesanan_2 = Pesanan("Pizza", 3)
print(pesanan_2.get_info())
print(pesanan_2.get_total_pesanan())

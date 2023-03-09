import multiprocessing
from myFunc import kasir

if __name__ == '__main__':
    items1 = {'produk1': 10000, 'produk2': 15000, 'produk3': 20000}
    items2 = {'produk4': 30000, 'produk5': 25000, 'produk6': 18000}
    
    process1 = multiprocessing.Process(target=kasir, args=(1, items1,))
    process2 = multiprocessing.Process(target=kasir, args=(2, items2,))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

# Hasilnya sebagai berikut :
# Kasir 1 melayani pelanggan...
# Kasir 1 memproses item produk1 dengan harga 10000
# Kasir 1 memproses item produk2 dengan harga 15000
# Kasir 1 memproses item produk3 dengan harga 20000
# Total harga untuk kasir 1: 45000
# Kasir 2 melayani pelanggan...
# Kasir 2 memproses item produk4 dengan harga 30000
# Kasir 2 memproses item produk5 dengan harga 25000
# Kasir 2 memproses item produk6 dengan harga 18000
# Total harga untuk kasir 2: 73000
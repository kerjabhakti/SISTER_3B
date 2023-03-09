import multiprocessing

def kasir(id_kasir, items):
    print(f'Kasir {id_kasir} melayani pelanggan...')
    total_harga = 0
    for item, harga in items.items():
        print(f'Kasir {id_kasir} memproses item {item} dengan harga {harga}')
        total_harga += harga
    print(f'Total harga untuk kasir {id_kasir}: {total_harga}')

if __name__ == '__main__':
    # daftar item yang dipesan pelanggan
    items1 = {'Kopi': 10000, 'Teh': 8000, 'Roti': 5000}
    items2 = {'Nasi Goreng': 25000, 'Ayam Goreng': 18000, 'Es Teh': 5000}
    items3 = {'Burger': 15000, 'Kentang Goreng': 12000, 'Cola': 6000}

    # membuat tiga kasir untuk melayani pelanggan
    kasir1 = multiprocessing.Process(target=kasir, args=(1, items1))
    kasir2 = multiprocessing.Process(target=kasir, args=(2, items2))
    kasir3 = multiprocessing.Process(target=kasir, args=(3, items3))

    # memulai tiga kasir secara paralel
    kasir1.start()
    kasir2.start()
    kasir3.start()

    # menunggu hingga ketiga kasir selesai melayani pelanggan
    kasir1.join()
    kasir2.join()
    kasir3.join()

# Hasilnya sebagai berikut :
# Kasir 2 melayani pelanggan...
# Kasir 2 memproses item Nasi Goreng dengan harga 25000
# Kasir 2 memproses item Ayam Goreng dengan harga 18000
# Kasir 2 memproses item Es Teh dengan harga 5000
# Total harga untuk kasir 2: 48000
# Kasir 1 melayani pelanggan...
# Kasir 1 memproses item Kopi dengan harga 10000
# Kasir 1 memproses item Teh dengan harga 8000
# Kasir 1 memproses item Roti dengan harga 5000
# Total harga untuk kasir 1: 23000
# Kasir 3 melayani pelanggan...
# Kasir 3 memproses item Burger dengan harga 15000
# Kasir 3 memproses item Kentang Goreng dengan harga 12000
# Kasir 3 memproses item Cola dengan harga 6000
# Total harga untuk kasir 3: 33000
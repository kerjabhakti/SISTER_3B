def kasir(id_kasir, items):
    print(f'Kasir {id_kasir} melayani pelanggan...')
    total_harga = 0
    for item, harga in items.items():
        print(f'Kasir {id_kasir} memproses item {item} dengan harga {harga}')
        total_harga += harga
    print(f'Total harga untuk kasir {id_kasir}: {total_harga}')
import multiprocessing

def pesan_baju(jenis_baju, ukuran, jumlah):
    print(f"Memproses pesanan {jumlah} {jenis_baju} ukuran {ukuran}...")
    print(f"Pesanan {jumlah} {jenis_baju} ukuran {ukuran} berhasil diproses.")

if __name__ == '__main__':
    pesanan = [
        {'jenis_baju': 'kaos', 'ukuran': 'M', 'jumlah': 5},
        {'jenis_baju': 'kemeja', 'ukuran': 'L', 'jumlah': 3},
        {'jenis_baju': 'celana', 'ukuran': 'XL', 'jumlah': 2},
        {'jenis_baju': 'jaket', 'ukuran': 'S', 'jumlah': 1}
    ]

    processes = []
    for p in pesanan:
        process = multiprocessing.Process(target=pesan_baju, args=(p['jenis_baju'], p['ukuran'], p['jumlah']))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

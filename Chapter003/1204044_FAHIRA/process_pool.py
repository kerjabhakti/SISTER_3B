import multiprocessing

def hitung_total(belanja):
    return sum(belanja)

if __name__ == '__main__':
    belanja_pelanggan = [[50000, 30000, 25000], [20000, 15000, 10000], [100000, 75000]]
    
    # Membuat process pool dengan 3 proses
    pool = multiprocessing.Pool(processes=3)
    
    # Menghitung total belanja untuk setiap pelanggan menggunakan process pool
    total_belanja = pool.map(hitung_total, belanja_pelanggan)
    
    # Menutup process pool
    pool.close()
    pool.join()
    
    # Menampilkan total belanja untuk setiap pelanggan
    for i, total in enumerate(total_belanja):
        print(f"Total belanja pelanggan {i+1} adalah Rp{total}")

# Hasilnya sebagai berikut :
# Total belanja pelanggan 1 adalah Rp105000
# Total belanja pelanggan 2 adalah Rp45000
# Total belanja pelanggan 3 adalah Rp175000
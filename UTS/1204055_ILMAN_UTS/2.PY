import multiprocessing
import time

def pesan_baju(jenis_baju, ukuran, jumlah):
    time.sleep(2)  
    print(f"Memproses pesanan {jumlah} {jenis_baju} ukuran {ukuran}...")
    time.sleep(6)  
    print(f"Pesanan {jumlah} {jenis_baju} ukuran {ukuran} berhasil diproses pada {time.ctime(time.time())}")

def kirim_baju(jenis_baju, ukuran, alamat):
    time.sleep(3)  
    print(f"Mengirim {jenis_baju} ukuran {ukuran} ke alamat {alamat}...")
    time.sleep(4)  
    print(f"{jenis_baju} ukuran {ukuran} berhasil dikirim ke alamat {alamat} pada {time.ctime(time.time())}")

if __name__ == '__main__':
    pesanan = [
        {'jenis_baju': 'kaos', 'ukuran': 'M', 'jumlah': 5},
        {'jenis_baju': 'kemeja', 'ukuran': 'L', 'jumlah': 3},
        {'jenis_baju': 'celana', 'ukuran': 'XL', 'jumlah': 2},
        {'jenis_baju': 'jaket', 'ukuran': 'S', 'jumlah': 1}
    ]

    processes = []
    for p in pesanan:
        process_baju = multiprocessing.Process(target=pesan_baju, args=(p['jenis_baju'], p['ukuran'], p['jumlah']))
        process_kirim = multiprocessing.Process(target=kirim_baju, args=(p['jenis_baju'], p['ukuran'], f"Jl. Raya No. {p['jumlah']*10}"))
        processes.append(process_baju)
        processes.append(process_kirim)
        process_baju.start()
        process_kirim.start()

    for process in processes:
        process.join()

    print("Semua pesanan telah diproses dan dikirim pada", {time.ctime(time.time())})

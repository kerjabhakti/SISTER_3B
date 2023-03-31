import multiprocessing

def antrean(nama_nasabah, antrean):
    antrean.put(nama_nasabah)
    print(f"{nama_nasabah} telah masuk ke dalam antrean.")

if __name__ == '__main__':
    antrean_nasabah = multiprocessing.Queue()
    processes = []

    # membuat antrean nasabah
    processes.append(multiprocessing.Process(target=antrean, args=("Sinta", antrean_nasabah)))
    processes.append(multiprocessing.Process(target=antrean, args=("Laura", antrean_nasabah)))
    processes.append(multiprocessing.Process(target=antrean, args=("Andre", antrean_nasabah)))
    
    # memulai proses untuk setiap antrean nasabah
    for process in processes:
        process.start()

    # menunggu sampai semua proses selesai
    for process in processes:
        process.join()

    # menampilkan antrean nasabah
    print("Antrean Nasabah:")
    while not antrean_nasabah.empty():
        print(antrean_nasabah.get())

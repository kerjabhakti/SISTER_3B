import multiprocessing
import time

def goride(passenger_name, destination):
    time.sleep(4)  # simulasi pemesanan dan perjalanan selama 4 detik
    print(f"{passenger_name} telah sampai di {destination} pada {time.ctime()}.")

def spawn_processes():
    passengers = ['Ilman', 'Nawaf', 'Daffa', 'Fadil']
    destinations = ['Mesjid Habiburahman', 'Mesjid Al-Hikmah', 'Mesjid Mekkah', 'Mesjid Madinah']
    processes = []

    start_time = time.time()

    for i in range(len(passengers)):
        p = multiprocessing.Process(target=goride, args=(passengers[i], destinations[i]))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Proses selesai dalam waktu {elapsed_time} detik.")

if __name__ == '__main__':
    spawn_processes()

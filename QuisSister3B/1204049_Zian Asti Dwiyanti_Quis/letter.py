import threading
import time

# definisi fungsi-fungsi untuk persiapan data surat, pembuatan surat, pengiriman surat, dan pelaporan hasil pengiriman

def prepare_data():
    print("[{}] Persiapan data surat dimulai...".format(time.strftime("%H:%M:%S")))
    time.sleep(2)
    print("[{}] Persiapan data surat selesai.".format(time.strftime("%H:%M:%S")))
    
def create_letter():
    print("[{}] Pembuatan surat dimulai...".format(time.strftime("%H:%M:%S")))
    time.sleep(3)
    print("[{}] Pembuatan surat selesai.".format(time.strftime("%H:%M:%S")))
    
def send_letter(lock):
    print("[{}] Pengiriman surat dimulai...".format(time.strftime("%H:%M:%S")))
    time.sleep(4)
    with lock:
        print("[{}] Pengiriman surat selesai.".format(time.strftime("%H:%M:%S")))
    
def report_delivery():
    print("[{}] Pelaporan hasil pengiriman dimulai...".format(time.strftime("%H:%M:%S")))
    time.sleep(2)
    print("[{}] Pelaporan hasil pengiriman selesai.".format(time.strftime("%H:%M:%S")))
    
# fungsi untuk menjalankan thread untuk setiap surat

def run_letter(letter_num, lock, barrier):
    prepare_data()
    create_letter()
    barrier.wait()
    send_letter(lock)
    report_delivery()
    print("[{}] Surat {} selesai dikirim.".format(time.strftime("%H:%M:%S"), letter_num))

# menjalankan proses utama dengan menggunakan thread

if __name__ == '__main__':
    print("[{}] Proses pengeksekusian beberapa pekerjaan dalam 1 waktu dimulai...\n".format(time.strftime("%H:%M:%S")))
    num_letters = 3
    threads = []
    lock = threading.Lock()
    barrier = threading.Barrier(num_letters + 1)
    for i in range(num_letters):
        t = threading.Thread(target=run_letter, args=(i+1, lock, barrier))
        threads.append(t)
        t.start()
    barrier.wait()
    for t in threads:
        t.join()
    print("\n[{}] Proses pengeksekusian beberapa pekerjaan dalam 1 waktu selesai.".format(time.strftime("%H:%M:%S")))

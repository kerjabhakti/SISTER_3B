import threading as tr
import time
from datetime import datetime

daftarTransaksi = ['Booth Soto', 'Booth Nasi', 'Booth Indomie', 'Booth Minuman', 'Booth Gorengan']

# Fungsi eksekusi thread
def proses_transaksi(barrier, transaksi_id):
    waktu = datetime.utcnow().strftime("%H:%M:%S.%f")
    print(f"Transaksi {transaksi_id} dimulai pada pukul {waktu}")
    time.sleep(4)
    waktu = datetime.utcnow().strftime("%H:%M:%S.%f")
    print(f"Transaksi {transaksi_id} selesai pada pukul {waktu}")
    barrier.wait()

def main():
    print("Input transaksi dimulai pada waktu:", datetime.utcnow().strftime("%H:%M:%S.%f"))

    # Membuat thread untuk setiap transaksi
    threads = []
    barrier = tr.Barrier(len(daftarTransaksi))
    for i, transaksi in enumerate(daftarTransaksi):
        threads.append(tr.Thread(target=proses_transaksi, args=(barrier, transaksi), name=f"Thread {i}"))

    # Memulai eksekusi setiap thread
    for thread in threads:
        thread.start()

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

    print("Semua transaksi selesai")
    print("Input transaksi selesai pada waktu:", datetime.utcnow().strftime("%H:%M:%S.%f"))

if __name__ == '__main__':
    main()

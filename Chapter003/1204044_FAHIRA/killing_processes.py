import multiprocessing
import time

def pembayaran():
    print('Sistem pembayaran sedang aktif.')
    total_harga = 0
    while True:
        item = input('Masukkan harga barang atau ketik "selesai" untuk keluar: ')
        if item == 'selesai':
            break
        total_harga += int(item)
        print(f'Item seharga {item} telah ditambahkan ke dalam keranjang belanja.')

    print('Menghitung total harga...')
    time.sleep(3)
    print(f'Total harga yang harus dibayar adalah {total_harga}.')

if __name__ == '__main__':
    p = multiprocessing.Process(target=pembayaran)
    print('Proses sebelum dieksekusi:', p, p.is_alive())
    p.start()
    print('Proses sedang berjalan:', p, p.is_alive())
    p.terminate()
    print('Proses telah dihentikan:', p, p.is_alive())
    p.join()
    print('Proses telah bergabung:', p, p.is_alive())
    print('Kode keluaran proses:', p.exitcode)

# Hasilnya sebagai berikut :
# Proses sebelum dieksekusi: <Process name='Process-1' parent=17648 initial> False
# Proses sedang berjalan: <Process name='Process-1' pid=13244 parent=17648 started> True
# Proses telah dihentikan: <Process name='Process-1' pid=13244 parent=17648 started> True
# Proses telah bergabung: <Process name='Process-1' pid=13244 parent=17648 stopped exitcode=-SIGTERM> False
# Kode keluaran proses: -15
import multiprocessing
import time

def buat_undangan(nama, tanggal, tempat):
    with open('undangan.txt', 'w') as f:
        f.write('Undangan Rapat\n\n')
        f.write('Kepada Yth.\n')
        f.write(f'{nama}\n\n')
        f.write(f'Diharapkan kehadiran pada tanggal {tanggal}\n')
        f.write(f'di {tempat}\n\n')
        f.write('Terima kasih\n')
    print(f'Undangan telah dibuat dan disimpan pada file "undangan.txt"')

def kirim_undangan(nama, email):
    # simulasi pengiriman email
    time.sleep(3)
    print(f'Undangan rapat telah dikirim ke {email}')

if __name__ == '__main__':
    nama = input('Masukkan nama yang diundang: ')
    email = input('Masukkan alamat email: ')
    tanggal = input('Masukkan tanggal rapat: ')
    tempat = input('Masukkan tempat rapat: ')

    start_time = time.time()

    p1 = multiprocessing.Process(target=buat_undangan, args=(nama, tanggal, tempat))
    p2 = multiprocessing.Process(target=kirim_undangan, args=(nama, email))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Program selesai.')

    end_time = time.time()

    print(f'Waktu eksekusi program: {end_time - start_time:.3f} detik')

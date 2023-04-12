import multiprocessing

def buat_undangan(nama, tanggal, tempat):
    with open('undangan.txt', 'w') as f:
        f.write('Undangan Rapat\n\n')
        f.write('Kepada Yth.\n')
        f.write(f'{nama}\n\n')
        f.write(f'Diharapkan kehadiran pada tanggal {tanggal}\n')
        f.write(f'di {tempat}\n\n')
        f.write('Terima kasih\n')
    print(f'Undangan telah dibuat dan disimpan pada file "undangan.txt"')

if __name__ == '__main__':
    nama = input('Masukkan nama yang diundang: ')
    tanggal = input('Masukkan tanggal rapat: ')
    tempat = input('Masukkan tempat rapat: ')

    p = multiprocessing.Process(target=buat_undangan, args=(nama, tanggal, tempat))
    p.start()
    p.join()

    print('Program selesai.')
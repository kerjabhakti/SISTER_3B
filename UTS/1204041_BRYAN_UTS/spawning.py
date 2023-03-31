import multiprocessing

# contoh data hasil mahasiswa (DHS)
DHS = {
    'Nawaf': [80, 85, 90],
    'Ilman': [70, 75, 80],
    'Fahira': [90, 95, 100],
    'Zian': [86, 75, 70]
}

def hitung_rata_rata(nama):
    nilai = DHS[nama]
    rata_rata = sum(nilai) / len(nilai)
    print(f"Rata-rata nilai {nama}: {rata_rata}")

if __name__ == '__main__':
    # membuat proses multiprocessing untuk setiap mahasiswa
    proses = []
    for nama in DHS.keys():
        p = multiprocessing.Process(target=hitung_rata_rata, args=(nama,))
        proses.append(p)
        p.start()

    # join semua proses agar tunggu semua proses selesai
    for p in proses:
        p.join()



# import multiprocessing

# def myFunc(i):
#     print ('calling myFunc from process n°: %s' %i)
#     for j in range (0,i):
#         print('output from myFunc is :%s' %j)
#     return

# if __name__ == '__main__':
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i,))
#         process.start()
#         process.join()



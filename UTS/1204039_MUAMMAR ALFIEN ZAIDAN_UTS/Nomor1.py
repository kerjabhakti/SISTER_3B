import multiprocessing

def spawnAyunan(jml):
    print ('Membuat kursi ayunan sejumlah: %s' %jml)
    for i in range (0,jml):
        print('Kursi ayunan yang telah jadi :%s' %i)
    return

if __name__ == '__main__':
    for i in range(7):
        process = multiprocessing.Process(target=spawnAyunan, args=(i,))
        process.start()
        process.join()

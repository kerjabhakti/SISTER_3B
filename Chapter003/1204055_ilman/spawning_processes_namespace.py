#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    print ('Mengerjakan tugas sistem tersebar Chapter: %s' %i)
    for j in range (0,i):
        print('Berhasil mengerjakan : Bagian %s' %j)
    return

if __name__ == '__main__':
    for i in range(10):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()

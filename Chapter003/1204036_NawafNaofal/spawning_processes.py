#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(hero):
    print('memanggil %s dari kelompok pahlawan' % hero)
    # kode untuk memanggil hero dari kelompok pahlawan
    return

heroes = ['Penyihir', 'Pendekar', 'Summoner']

for hero in heroes:
    myFunc(hero)

if __name__ == '__main__':
    for i in range(0):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()


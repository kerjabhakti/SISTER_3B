#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    print ('WC %s' %i)
    for j in range (1,i):
        print('Urutan ke %s' %j ,'masuk')
    return

if __name__ == '__main__':
    for i in range(10):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()


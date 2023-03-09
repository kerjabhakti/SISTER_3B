import multiprocessing

def myFunc(matakuliah):
    print('memanggil mata kuliah %s' % matakuliah)
    return

matakuliahs = ['SISTER', 'AI', 'DATA MINING']

for matakuliah in matakuliahs:
    myFunc(matakuliah)


if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
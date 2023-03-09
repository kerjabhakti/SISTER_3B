import multiprocessing

class kamar(multiprocessing.Process):

    def run(self):
        print ('Bapak kos cek %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(7):
        process = kamar()
        process.start()
        process.join()


import multiprocessing

class Transaksi(multiprocessing.Process):

    def run(self):
        print ('Transaksi Done Kakak, Abang :) %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(4):
        process = Transaksi()
        process.start()
        process.join()
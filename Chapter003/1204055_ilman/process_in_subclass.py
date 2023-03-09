import multiprocessing

class Pemesanan(multiprocessing.Process):

    def run(self):
        print ('%s berhasil di proses!' %self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = Pemesanan()
        process.start()
        process.join()

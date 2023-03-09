import multiprocessing


class Antrian(multiprocessing.Process):

    def run(self):
        print('Nomor %s Sudah di proses!' % self.name)
        return


if __name__ == '__main__':
    for i in range(10):
        process = Antrian()
        process.start()
        process.join()

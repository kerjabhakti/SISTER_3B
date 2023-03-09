import multiprocessing

class StockProcess(multiprocessing.Process):
    def run(self):
        print("Check stock process name = %s \n" %self.name)
        return

if __name__ == '__main__':
    for i in range(5):
        process = StockProcess()
        process.start()
        process.join()

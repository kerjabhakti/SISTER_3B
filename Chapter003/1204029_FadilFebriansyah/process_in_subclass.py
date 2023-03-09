import multiprocessing

class MyTask(multiprocessing.Process):

    def run(self):
        print ('Sedang mengerjakan tugas chapter 3 %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyTask()
        process.start()
        process.join()
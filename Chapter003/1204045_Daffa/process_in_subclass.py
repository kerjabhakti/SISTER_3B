import multiprocessing

class MyProcess(multiprocessing.Process):
    
    def __init__(self, surah, ayat):
        multiprocessing.Process.__init__(self)
        self.surah = surah
        self.ayat = ayat
        
    def run(self):
        print(f"Reading Surah {self.surah}, ayat {self.ayat}...")
        # Implement code to retrieve and print the verse here
        
if __name__ == '__main__':
    processes = []
    for i in range(3):
        process = MyProcess(i+1, i+1)
        process.start()
        processes.append(process)
        
    for process in processes:
        process.join()

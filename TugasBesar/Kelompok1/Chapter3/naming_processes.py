import multiprocessing
import time

def collectTask():
    name = multiprocessing.current_process().name
    print("Mengumpulkan tugas = %s \n" % name)
    time.sleep(3)
    print("Selesai mengumpulkan tugas = %s \n" % name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='Pengumpulan Tugas 1', target=collectTask)

    #process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process(target=collectTask)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()

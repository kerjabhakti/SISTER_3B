import threading
import queue
import time

q = queue.Queue()

def isi_queue():
    print("Thread isi_queue dimulai pada waktu {}".format(time.ctime()))
    tagihan = ["Listrik", "Air", "Telepon", "Internet"]
    for item in tagihan:
        q.put(item)
        print("Menambahkan tagihan {} ke dalam queue pada waktu {}".format(item, time.ctime()))
        time.sleep(1)
    print("Thread isi_queue selesai pada waktu {}".format(time.ctime()))

def proses_tagihan():
    print("Thread proses_tagihan dimulai pada waktu {}".format(time.ctime()))
    while not q.empty():
        tagihan = q.get()
        print("Memproses tagihan {} pada waktu {}".format(tagihan, time.ctime()))
        time.sleep(2)
    print("Thread proses_tagihan selesai pada waktu {}".format(time.ctime()))

t1 = threading.Thread(target=isi_queue)

t2 = threading.Thread(target=proses_tagihan)

t1.start()
t2.start()

t1.join()
t2.join()

print("Semua tagihan telah diproses pada waktu {}".format(time.ctime()))

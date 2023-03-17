import threading
import time
import queue
from datetime import datetime, timedelta

print("Program dimulai pada", datetime.now().strftime("%A, %d %B %Y %H:%M:%S"))
print("----------------------------------------------------------------------")

def daftar(nama, queue):
    time.sleep(2)
    waktu = datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    print(f"{nama} telah mendaftar pada waktu {waktu}")
    queue.put((nama, waktu))

def seleksi(queue):
    while True:
        if not queue.empty():
            nama, waktu = queue.get()
            time.sleep(3)
            if nama == "Dadang":
                waktu_seleksi = datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
                print(f"{nama} diterima pada waktu {waktu_seleksi}")
            else:
                waktu_seleksi = datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
                print(f"{nama} ditolak pada waktu {waktu_seleksi}")
        else:
            break

q = queue.Queue()
t_daftar = []
t_seleksi = threading.Thread(target=seleksi, args=(q,))

for nama in ["Dadang", "Dani", "Kusnadi", "Mansur"]:
    t = threading.Thread(target=daftar, args=(nama, q))
    t_daftar.append(t)
    t.start()

for t in t_daftar:
    t.join()

start_time = datetime.now()

t_seleksi.start()
t_seleksi.join()

end_time = datetime.now()

total_time = end_time - start_time

total_time_str = str(total_time).split(".")[0]
total_time_formatted = datetime.strptime(total_time_str, "%H:%M:%S")

print("----------------------------------------------------------------------")
print(f"Waktu seleksi dimulai pada: {start_time.strftime('%A, %d %B %Y %H:%M:%S')}")
print(f"Waktu seleksi selesai pada: {end_time.strftime('%A, %d %B %Y %H:%M:%S')}")
print(f"-------------- Total waktu seleksi: {total_time_formatted.strftime('%H:%M:%S')} -------------- ")
print("----------------------------------------------------------------------")
print("Program selesai pada", datetime.now().strftime("%A, %d %B %Y %H:%M:%S"))

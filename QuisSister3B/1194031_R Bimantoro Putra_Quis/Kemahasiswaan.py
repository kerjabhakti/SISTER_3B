import threading
import time

# variabel global yang akan digunakan oleh beberapa thread
students = {'Matt': 0, 'Bima': 0, 'Putra': 0}
lock = threading.Lock()

# fungsi yang akan dijalankan oleh thread
def student_func(barrier, student_name, score):
    global students

    # menggunakan lock untuk memastikan variabel students tidak diakses oleh thread lain pada saat yang sama
    with lock:
        students[student_name] += score
        print(f'{student_name} Mendapat Nilai {score} ')
        print(f'Data Nilai: {students}')

    # memanggil perintah wait() pada barrier untuk menunggu thread lain selesai
    barrier.wait()
    print(f'Nilai {student_name} telah di input ')

if __name__ == '__main__':
    # daftar tugas yang akan dijalankan
    tasks = [('Matt', 5), ('Bima', 10), ('Putra', 7)]

    # membuat barrier dengan jumlah thread yang sama dengan jumlah tugas
    barrier = threading.Barrier(len(tasks))

    # buat thread baru untuk setiap tugas
    threads = []
    for task in tasks:
        student_name, score = task
        t = threading.Thread(target=student_func, args=(barrier, student_name, score))
        threads.append(t)

    # jalankan thread-thread tersebut secara bersamaan
    start_time = time.time()
    for t in threads:
        t.start()
        print(f'{t.name} Mulai {time.time()}')

    # tunggu semua thread selesai
    for t in threads:
        t.join()
        print(f'{t.name} Selesai {time.time()}')

    end_time = time.time()
    print(f'Semua selesai dalam waktu waktu {end_time-start_time:.2f} seconds')
    print(f'Nilai Akhir Mahasiswa adalah: {students}')
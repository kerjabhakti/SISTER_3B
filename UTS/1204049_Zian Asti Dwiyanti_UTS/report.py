import multiprocessing
import time

# fungsi untuk menghitung jumlah permintaan dukungan dan waktu respon rata-rata
def helpdesk_report(queue):
    requests = [10, 15, 20, 25, 30] # jumlah permintaan dukungan per hari selama 5 hari
    response_times = [5, 7, 10, 8, 12] # waktu respon rata-rata per hari selama 5 hari
    
    # hitung jumlah permintaan dukungan dan waktu respon rata-rata selama 5 hari
    total_requests = sum(requests)
    avg_response_time = sum(response_times) / len(response_times)
    
    # kirim hasil perhitungan ke antrian (queue)
    queue.put((total_requests, avg_response_time))

# fungsi untuk menghitung waktu menerima request dukungan
def time_of_day():
    return time.strftime("%H:%M:%S")

if __name__ == '__main__':
    # buat antrian (queue) untuk mengirim hasil perhitungan dari proses
    queue = multiprocessing.Queue()
    
    # buat proses baru untuk menghitung jumlah permintaan dukungan dan waktu respon rata-rata
    p1 = multiprocessing.Process(target=helpdesk_report, args=(queue,))
    p1.start()
    
    # buat proses baru untuk menghitung waktu menerima request dukungan
    p2 = multiprocessing.Process(target=time_of_day)
    p2.start()
    
    # tunggu kedua proses selesai
    p1.join()
    p2.join()
    
    # ambil hasil perhitungan dari antrian
    total_requests, avg_response_time = queue.get()
    
    # ambil waktu menerima request dukungan dari proses kedua
    time_received = time.time()
    
    # tampilkan hasil perhitungan dan waktu menerima request dukungan
    print(f"Jumlah permintaan dukungan selama 5 hari: {total_requests}")
    print(f"Waktu respon rata-rata selama 5 hari: {avg_response_time}")
    print(f"Waktu menerima request dukungan: {time_received}")

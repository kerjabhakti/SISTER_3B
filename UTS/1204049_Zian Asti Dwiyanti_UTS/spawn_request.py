import multiprocessing

# Fungsi untuk memproses permintaan dukungan
def process_support_request(request):
    # Kode untuk memproses permintaan dukungan
    print(f"Memproses permintaan dukungan {request}...")

# Fungsi untuk membuat antrian permintaan dukungan
def create_support_request_queue():
    # Kode untuk membuat antrian permintaan dukungan
    return multiprocessing.Queue()

# Fungsi untuk menambahkan permintaan dukungan ke dalam antrian
def add_support_request_to_queue(request, request_queue):
    # Kode untuk menambahkan permintaan dukungan ke dalam antrian
    request_queue.put(request)

# Fungsi untuk mengambil permintaan dukungan dari antrian dan memprosesnya
def process_support_requests(request_queue):
    # Kode untuk mengambil permintaan dukungan dari antrian dan memprosesnya
    while True:
        request = request_queue.get()
        if request is None:
            break
        process_support_request(request)

if __name__ == '__main__':
    # Membuat antrian permintaan dukungan
    request_queue = create_support_request_queue()

    # Menambahkan permintaan dukungan ke dalam antrian
    add_support_request_to_queue("Ke-1", request_queue)
    add_support_request_to_queue("ke-2", request_queue)
    add_support_request_to_queue("Ke-3", request_queue)
    add_support_request_to_queue("Ke-4", request_queue)
    add_support_request_to_queue("Ke-5", request_queue)

    # Menentukan jumlah proses yang akan di-spawn
    num_processes = 3

    # Menambahkan sentinal value ke dalam antrian sebagai tanda bahwa tidak akan ada lagi permintaan dukungan
    for i in range(num_processes):
        request_queue.put(None)

    # Men-spawn proses untuk memproses permintaan dukungan
    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=process_support_requests, args=(request_queue,))
        p.start()
        processes.append(p)

    # Menunggu hingga semua permintaan dukungan selesai diproses
    for p in processes:
        p.join()

    # Memberitahu bahwa semua permintaan dukungan sudah selesai diproses
    print("Semua permintaan dukungan selesai diproses.")

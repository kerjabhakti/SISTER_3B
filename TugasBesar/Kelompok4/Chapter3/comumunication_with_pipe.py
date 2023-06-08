import multiprocessing 

def antrian_luxury(pipe):
    output_pipe, _ = pipe
    for kupon in range(1, 10):
        # Check In Antrian
        print("Check in Antrian di Auto's Luxury: -77"+str(kupon))
        output_pipe.send(kupon + kupon)
    output_pipe.close()
 
def kupon_antrian(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            kupon = input_pipe.recv()
            print("Mendapatkan Kupon Antrian di Auto's Luxury : "+str(kupon))
            output_pipe.send(kupon)
    except EOFError:
        output_pipe.close()
 
def memilih_mobil():
    # Pengguna dapat melihat detail mobil yang menarik minatnya
    print("Daftar Mobil yang Tersedia:")
    print("1. Mobil Mewah A")
    print("2. Mobil Mewah B")
    print("3. Mobil Mewah C")
    
    pilihan = input("Pilih nomor mobil yang ingin dipesan: ")

    # Melakukan pilihan mobil
    print(f"Anda telah memilih Mobil Mewah {pilihan} untuk dipesan.")

if __name__ == '__main__':
    # First process pipe with slide numbers
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=antrian_luxury, args=(pipe_1,))
    process_pipe_1.start()

    # Second pipe
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=kupon_antrian, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(f"Kode Unik yang diperoleh: {pipe_2[1].recv()}-77")
            memilih_mobil()
    except EOFError:
        print("Selesai: proses Pengantrian & Pembagian Kupon Auto's Luxury")

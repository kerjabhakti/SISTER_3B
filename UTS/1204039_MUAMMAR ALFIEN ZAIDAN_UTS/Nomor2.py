import multiprocessing
import time

def jalankanKomidiPutar():
    print("Komidi Putar sedang berjalan.")
    time.sleep(2)

def jalankanHisteria():
    print("Histeria sedang berjalan.")
    time.sleep(3)

if __name__ == "__main__":
    # jalanin timer
    start_time = time.time()

    # inisiasi proses
    p1 = multiprocessing.Process(target=jalankanKomidiPutar)
    p2 = multiprocessing.Process(target=jalankanHisteria)

    # jalanin proses
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # itung waktu proses yg jalan
    elapsed_time = time.time() - start_time
    print(f"Waktu proses wahana: {elapsed_time:.2f} detik")

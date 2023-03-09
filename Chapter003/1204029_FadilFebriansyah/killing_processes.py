import multiprocessing
import time

def hitung_nilai(nilai):
    print('Starting function')
    total = sum(nilai)
    rata_rata = total / len(nilai)
    print('Rata-rata nilai:', rata_rata)
    time.sleep(1)
    print('Finished function')

if __name__ == '__main__':
    nilai_mahasiswa = [80, 70, 90, 85, 75, 95, 65, 75, 80, 85]

    p = multiprocessing.Process(target=hitung_nilai, args=(nilai_mahasiswa,))
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)

import multiprocessing
import time

## mengubah function foo dengan studi kasus yang disesuaikan
def petualang(name):
    print('Petualang', name, 'Memasuki dungeon')
    time.sleep(2)
    print('Petualang', name, 'Bertemu dengan monster')
    time.sleep(2)
    print('Petualang', name, 'Mencoba untuk melawan monster')
    time.sleep(2)
    print('Petualang', name, 'Terkena serangan oleh monster dan terbunuh')

if __name__ == '__main__':
    processes = []
    for name in ['Dadang', 'Andi', 'Trisno']:
        p = multiprocessing.Process(target=petualang, args=(name,))
        processes.append(p)
        print('Process before execution:', p, p.is_alive())
        p.start()
        print('Process running:', p, p.is_alive())
        # p.terminate()
        # print('Process terminated:', p, p.is_alive())
        p.join()
        print('Process joined:', p, p.is_alive())
        print('Process exit code:', p.exitcode)
    print('Semua petualang terbunuh!')

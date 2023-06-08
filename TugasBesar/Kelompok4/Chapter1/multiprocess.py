import multiprocessing
import time

def register(username):
    print(f"Proses pendaftaran pengguna {username} dimulai")
    time.sleep(2)  # Simulasi waktu yang dibutuhkan untuk pendaftaran
    print(f"Proses pendaftaran pengguna {username} selesai")

def login(username):
    print(f"Proses login pengguna {username} dimulai")
    time.sleep(1)  # Simulasi waktu yang dibutuhkan untuk login
    print(f"Proses login pengguna {username} selesai")

if __name__ == '__main__':
    usernames = ['Bryan', 'Sapwang', 'Ilman']

    processes = []
    for username in usernames:
        registration_process = multiprocessing.Process(target=register, args=(username,))
        processes.append(registration_process)
        registration_process.start()

    for process in processes:
        process.join()

    processes = []
    for username in usernames:
        login_process = multiprocessing.Process(target=login, args=(username,))
        processes.append(login_process)
        login_process.start()

    for process in processes:
        process.join()
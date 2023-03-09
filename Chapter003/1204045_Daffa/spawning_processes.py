import multiprocessing

def read_quran(target):
    print(f"{target} starts reading Quran")
    for ayat in range(1, 5):
        print(f"{target} reads ayat {ayat}")
    print(f"{target} finishes reading Quran")

if __name__ == '__main__':
    for target in range(1, 4):
        process = multiprocessing.Process(target=read_quran, args=(f"Target {target}",))
        process.start()

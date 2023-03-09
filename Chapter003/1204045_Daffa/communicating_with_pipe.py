##Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing 
import random

# daftar ayat Al-Quran yang akan dibaca
quran_verses = [
    'Bismillāhir-raḥmānir-raḥīm(i).',
    'Al-ḥamdu lillāhi rabbil-‘ālamīn(a).',
    'Ar-raḥmānir-raḥīm(i).',
    'Māliki yaumid-dīn(i).',
    'Iyyāka na‘budu wa iyyāka nasta‘īn(u),',
    'Ihdinaṣ-ṣirāṭal-mustaqīm(a).',
    'Ṣirāṭal-lażīna an‘amta ‘alaihim',
    'gairil-magḍūbi ‘alaihim',
    'wa laḍ-ḍāllīn(a).'
]

def create_items(pipe):
    output_pipe, _ = pipe
    for verse in quran_verses:
        # kirim ayat ke proses selanjutnya
        output_pipe.send(verse)
    output_pipe.close()
 
def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            # terima ayat dari proses sebelumnya
            verse = input_pipe.recv()
            # simulasi membaca ayat dalam waktu acak antara 1-5 detik
            read_time = random.randint(1, 5)
            print(f"Sedang membaca '{verse}', waktu: {read_time} detik")
            # kirim waktu baca ke proses selanjutnya
            output_pipe.send(read_time)
    except EOFError:
        output_pipe.close()
 
 
if __name__== '__main__':

    # pipe pertama untuk mengirim ayat
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    # pipe kedua untuk menerima waktu baca
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()
 
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            # menerima waktu baca dan menampilkan ke layar
            read_time = pipe_2[1].recv()
            print(f"Selesai membaca dalam waktu {read_time} detik")
    except EOFError:
        print("End")

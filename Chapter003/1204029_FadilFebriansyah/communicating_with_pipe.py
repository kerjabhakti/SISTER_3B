import multiprocessing 

def do_task(pipe):
    output_pipe, _ = pipe
    for task in range(10):
        print('Mengerjakan Tugas : '+str(task))
        output_pipe.send("Tugas " + str(task) + " selesai.")
    output_pipe.close()

def process_results(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            task = input_pipe.recv()
            print('Hasil Tugas: ' + str(task))
            output_pipe.send("Tugas " + str(task) + " berhasil diproses.")
    except EOFError:
        output_pipe.close()

if __name__ == '__main__':

    pipe_1 = multiprocessing.Pipe(True)
    task_process = multiprocessing.Process(target=do_task, args=(pipe_1,))
    task_process.start()

    pipe_2 = multiprocessing.Pipe(True)
    result_process = multiprocessing.Process(target=process_results, args=(pipe_1, pipe_2,))
    result_process.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print ("Semua tugas selesai.")

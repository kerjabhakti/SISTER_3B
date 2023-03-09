import multiprocessing 
import time

def play_slide(pipe):
    output_pipe, _ = pipe
    for i in range(3):
        print(f"Anak sedang bermain di ayunan {i+1}")
        time.sleep(1)
        output_pipe.send(i+1)
    output_pipe.close()

def play_swing(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            print(f"Anak sedang bermain perosotan di tinggi {item} meter")
            time.sleep(1)
            output_pipe.send(item)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':

    #First process pipe with slide numbers
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = \
                   multiprocessing.Process\
                   (target=play_slide, args=(pipe_1,))
    process_pipe_1.start()

    #second pipe,
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
                   multiprocessing.Process\
                   (target=play_swing, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            
            print (f"Anak turun dari perosotan setelah {pipe_2[1].recv()} meter")
    except EOFError:
        print ("Anak sudah selesai bermain di taman")

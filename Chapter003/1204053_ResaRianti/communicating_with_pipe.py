import multiprocessing 
import time

def customer_service(pipe):
    output_pipe, _ = pipe
    for i in range(5):
        print(f"Customer service is ready to serve {i+1}")
        time.sleep(1)
        output_pipe.send(i+1)
    output_pipe.close()

def teller(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            request = input_pipe.recv()
            print(f"Please enter your request: {request} ")
            time.sleep(1)
            output_pipe.send(request)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':

    # First process pipe with customer requests
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = \
                   multiprocessing.Process\
                   (target=customer_service, args=(pipe_1,))
    process_pipe_1.start()
    
    # Second pipe with customer service responses
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
                   multiprocessing.Process\
                   (target=teller, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            
            print (f"Your request {pipe_2[1].recv()} has been processed")
    except EOFError:
        print ("Customer has left the bank")

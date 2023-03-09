import multiprocessing

def supplier(pipe):
    output_pipe, _ = pipe
    for stock in range(10):
        print(f"Supplier menambahkan stock: {stock}")
        output_pipe.send(stock)
    output_pipe.close()

def stock_manager(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            stock = input_pipe.recv()
            print(f"Stock setelah ditambahkan: {stock*stock}")
            output_pipe.send(stock * stock)
    except EOFError:
        output_pipe.close()

if __name__ == '__main__':
    # First process pipe with items from supplier
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=supplier, args=(pipe_1,))
    process_pipe_1.start()

    # Second pipe for stock management
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=stock_manager, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            stock = pipe_2[1].recv()
            print(f"Stock terbaru: {stock}")
    except EOFError:
        print("Proses selesai")

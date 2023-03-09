import multiprocessing

def kasir(input_pipe, output_pipe):
    total_harga = 0
    try:
        while True:
            item = input_pipe.recv()
            if item == 'selesai':
                break
            harga = item * 1000
            total_harga += harga
            output_pipe.send(harga)
        output_pipe.send(total_harga)
    except EOFError:
        input_pipe.close()
        output_pipe.close()

if __name__ == '__main__':
    pipe_kasir = multiprocessing.Pipe(True)
    pipe_pelanggan = multiprocessing.Pipe(True)

    process_kasir = multiprocessing.Process(target=kasir, args=(pipe_pelanggan[0], pipe_kasir[1]))
    process_kasir.start()

    total_belanja = 0
    for item in [3, 4, 1, 5]:
        pipe_pelanggan[1].send(item)
        harga = pipe_kasir[0].recv()
        print(f"pelanggan membeli {item} item dengan harga {harga}")
        total_belanja += harga

    pipe_pelanggan[1].send('selesai')
    total_harga = pipe_kasir[0].recv()
    print(f"Total belanja pelanggan adalah {total_harga}")

    process_kasir.join()

# Hasilnya sebagai berikut :
# pelanggan membeli 3 item dengan harga 3000
# pelanggan membeli 4 item dengan harga 4000
# pelanggan membeli 1 item dengan harga 1000
# pelanggan membeli 5 item dengan harga 5000
# Total belanja pelanggan adalah 13000
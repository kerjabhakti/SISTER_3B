##Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing


def create_items(pipe):
    output_pipe, _ = pipe
    items = ["Potion", "Sword", "Shield", "Armor", "Ring", "Amulet", "Scroll", "Staff", "Wand", "Bow"]
    for item in items:
        print('Output pipe yang dikirim dari create_items: '+ item)
        output_pipe.send(item)
    output_pipe.close()

def process_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            print('Output pipe yang dikirim dari process_items: Item yang diperkuat ' + item )
            output_pipe.send('Item yang diperkuat ' +  item)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':

#Membuat item game menggunakan pipe
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = \
                    multiprocessing.Process\
                    (target=create_items, args=(pipe_1,))
    process_pipe_1.start()

#Meng-enchant item game menggunakan pipe lain,
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
                    multiprocessing.Process\
                    (target=process_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            
            enchanted_item = pipe_2[1].recv()
            print('Item yang telah diperkuat : ' + enchanted_item)
    except EOFError:
        print ("End of game")
    

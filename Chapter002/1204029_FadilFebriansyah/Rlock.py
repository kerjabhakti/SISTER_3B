import threading
import time
import random


class Kitchen:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def cook(kitchen, dishes):
    print("Memasak {} hidangan \n".format(dishes))
    while dishes:
        kitchen.add()
        time.sleep(1)
        dishes -= 1
        print("Memasak satu hidangan --> {} hidangan tersedia \n".format(dishes))


def serve(kitchen, dishes):
    print("Melayani {} hidangan \n".format(dishes))
    while dishes:
        kitchen.remove()
        time.sleep(1)
        dishes -= 1
        print("Melayani satu hidangan --> {} hidangan tersedia \n".format(dishes))


def main():
    dishes = random.randint(10, 20)
    kitchen = Kitchen()

    t1 = threading.Thread(target=cook, \
                          args=(kitchen, dishes))
    t2 = threading.Thread(target=serve, \
                          args=(kitchen, random.randint(1, dishes)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
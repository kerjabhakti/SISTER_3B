import threading
import time
import random


class Stock:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add_item(self):
        with self.lock:
            self.execute(1)

    def remove_item(self):
        with self.lock:
            self.execute(-1)

def supplier(stock, items):
    print("Supplier is adding {} items to stock".format(items))
    while items:
        stock.add_item()
        time.sleep(1)
        items -= 1
        print("ADDED one item -->{} item to ADD \n".format(items))



def customer(stock, items):
    print("Customer is buying {} items from stock".format(items))
    while items:
        stock.remove_item()
        time.sleep(1)
        items -= 1
        print("REMOVED one item -->{} item to REMOVE \n".format(items))


def main():
    items = 10
    stock = Stock()

    t1 = threading.Thread(target=supplier, \
                          args=(stock, random.randint(10,20)))
    t2 = threading.Thread(target=customer, \
                          args=(stock, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
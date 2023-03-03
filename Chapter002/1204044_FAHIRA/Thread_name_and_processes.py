 # terdapat 2 thread, yaitu Kasir dan Penjual. 
 # Penjual akan menambahkan item ke dalam list 
 # items dan memberitahu Kasir melalui event bahwa 
 # ada item baru yang ditambahkan. Kemudian Kasir 
 # akan mengambil item tersebut dari list items dan 
 # memberitahu bahwa item telah diambil. 
 # Program akan terus berjalan sampai dihentikan secara paksa.

from threading import Thread
import time
import os
import msvcrt

class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.total = 0

    def run(self):
        while True:
            item = input("Enter item name (or 'exit' to stop): ")
            if item.lower() == 'exit':
                break
            price = float(input("Enter item price: "))
            self.total += price
            print(f"{item} added to cart ({price:.2f} $)")

        print(f"Total: {self.total:.2f} $")

    def stop(self):
        self._stop_event.set()

def main():
    thread1 = MyThreadClass("Thread#1")

    # Thread Running
    thread1.start()

    # Wait for the thread to finish or for the user to press ESC
    while thread1.is_alive():
        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
            print("\nExiting...")
            thread1.stop()
            thread1.join()
            return

    # End 
    print("End")

if __name__ == "__main__":
    main()


# Enter item name (or 'exit' to stop): sabun
# Enter item price: 10000
# sabun added to cart (10000.00 $)
# Enter item name (or 'exit' to stop): exit
# Total: 10000.00 $
# End

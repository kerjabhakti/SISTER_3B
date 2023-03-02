import time
import os
from random import randint
from threading import Thread

class MyThreadClass (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " berjalan, dengan process ID "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " over\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    anak1 = MyThreadClass("Anak#1 ", randint(1,10))
    anak2 = MyThreadClass("Anak#2 ", randint(1,10))
    anak3 = MyThreadClass("Anak#3 ", randint(1,10))
    anak4 = MyThreadClass("Anak#4 ", randint(1,10))
    anak5 = MyThreadClass("Anak#5 ", randint(1,10))
    anak6 = MyThreadClass("Anak#6 ", randint(1,10))
    anak7 = MyThreadClass("Anak#7 ", randint(1,10))
    anak8 = MyThreadClass("Anak#8 ", randint(1,10))
    anak9 = MyThreadClass("Anak#9 ", randint(1,10))

    # Anak Running
    anak1.start()
    anak2.start()
    anak3.start()
    anak4.start()
    anak5.start()
    anak6.start()
    anak7.start()
    anak8.start()
    anak9.start()

    # Anak joining
    anak1.join()
    anak2.join()
    anak3.join()
    anak4.join()
    anak5.join()
    anak6.join()
    anak7.join()
    anak8.join()
    anak9.join()

    # End 
    print("Selesai")

    #Execution Time
    print("Durasi seluruh proses: %s detik ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

# import threading
# import time

# def MyThreadClass(nama, urutan):
#     for i in range(urutan):
#         print(nama, i)
#         time.sleep(0.5)

# def main():
#     # Create threads
#     anak1 = threading.Thread(target=MyThreadClass, args=("Anak Pertama", 5))
#     anak2 = threading.Thread(target=MyThreadClass, args=("Anak Kedua", 5))

#     start_time = time.time()

#     # Start threads
#     anak1.start()
#     anak2.start()

#     # Wait for threads to finish
#     anak1.join()
#     anak2.join()

#     # Print final message
#     print("Selesai")

#     #Execution Time
#     print("Durasi seluruh proses: %s detik ---" % (time.time() - start_time))

# if __name__ == '__main__':
#     main()
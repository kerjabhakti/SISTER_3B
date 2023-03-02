from threading import Thread
import time
import os

class kontrakan (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name

  
   def run(self):
       
       print("Kamar telah di isi oleh {}".format(self.name)) 

def main():
    from random import randint
    #pembuatan thread
    anngota1 = kontrakan("Miracle ")
    anggota2 = kontrakan("Sumiya")
    anggota3 = kontrakan("Bruno")
    anggota4 = kontrakan ("Pudge")
    anggota5 = kontrakan ("Poltekpos")
    
    anngota1.start()
    anggota2.start()
    anggota3.start()
    anggota4.start()
    anggota5.start()


    
    anngota1.join()
    anggota2.join()
    anggota3.join()
    anggota4.join()
    anggota5.join()


    print("Semua kamar telah di isi")


if __name__ == "__main__":
    main()

    



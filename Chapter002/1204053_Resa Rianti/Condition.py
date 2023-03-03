import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

available = []
condition = threading.Condition()

class Client(threading.Thread):
    def __init__(self, name, clientStored, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.clientStored = clientStored

    def deposit(self):
        
        with condition:
            
            if len(available) == 0:
                logging.info('tidak ada transaksi yang tersedia')
                condition.wait()
                
            available.pop()
            self.clientStored += 1
            logging.info('%s transaksi ditambahkan %d', self.name, self.clientStored)
            
            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.deposit()

class ClientStored(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def newClientStored(self):
        
        with condition:
            
            if len(available) == 10:
                logging.info('Setoran sudah diterima')
                condition.wait()
                
            available.append(1)
            logging.info('setoran baru, maka %d', len(available))
            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.2)
            self.newClientStored()

def main():
    nClient = [Client(name=name, clientStored=10) for name in ['Billa', 'Raka', 'Riri', 'Dilan', 'Nisa', 'Rehan', 'Muti', 'Sipa', 'Ronald', 'Ojan']]
    cStored = ClientStored(name='Nasabah')

    for client in nClient:
        client.start()

    
    cStored.start()

    for client in nClient:
        client.join()

    cStored.join()

if __name__ == "__main__":
    main()
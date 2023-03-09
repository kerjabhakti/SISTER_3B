import multiprocessing

class Service(multiprocessing.Process):

    def __init__(self, customer):
        super(Service, self).__init__()
        self.customer = customer

    def run(self):
        print('Nasabah %d sudah memasuki bagian pelayanan' % self.customer)
        return
       
if __name__ == '__main__':
    for i in range(10):
        process = Service(i)
        process.start()
        process.join()
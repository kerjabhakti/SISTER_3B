import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Silakan " + str (name) + " tunggu nilai anda di website E-Learning")

def startServer():
    server = Server()
    # buat daemon pyro
    daemon = Pyro4.Daemon()             
    # mencari nameserver yang berjalan
    ns = Pyro4.locateNS()
    # mendaftarkan server sebagai objek pyro
    uri = daemon.register(server)  
    # mendaftarkan objek dengan nama di nameserver
    ns.register("server", uri)   
    # melakukan print url nya agar dapat digunakan di-client
    print("Ready. Object uri =", uri)
    # jalankan loop pengecekan untuk menunggu request dari client
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()


import Pyro4


class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return "Selamat datang di layanan pemesanan makanan, " + str(name) + "!"

    @Pyro4.expose
    def placeOrder(self, menu, quantity):
        # Di sini Anda dapat menambahkan logika untuk memproses pemesanan makanan
        # dan mengembalikan pesan konfirmasi
        return (
            "Pesanan Anda untuk " + str(quantity) + " " + str(menu) + " telah diterima."
        )


def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("server", uri)
    print("Server siap. Object URI =", uri)
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()

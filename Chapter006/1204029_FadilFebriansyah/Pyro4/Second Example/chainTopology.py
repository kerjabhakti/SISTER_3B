import Pyro4

@Pyro4.expose
class Chain(object):
    def __init__(self, name, current_server):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None
    
    def process(self, message):
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        if self.name in message:
            print("Kembali ke pesanan %s; Makanan akan di kirim kembali!" % self.name)
            return ["Kembali ke Makanan " + self.name]
        else:
            print("Makanan %s sudah selesai diantarkan dilanjutkan dengan makanan selanjutnya %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "Makanan" + self.name + " sudah selesai dikirim")
            return result

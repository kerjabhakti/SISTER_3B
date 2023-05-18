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
            print("Kembali ke buku %s; Buku akan di ulang dari halaman 1" % self.name)
            return ["Kembali ke buku " + self.name]
        else:
            print("Buku %s sudah selesai di baca lanjutkan ke buku %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "Buku " + self.name + " sudah selesai di baca!")
            return result

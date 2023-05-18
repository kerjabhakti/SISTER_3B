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
            print("Kamu belum membership %s; Gagal bergabung ke The Lookout's! " % self.name)
            return ["Coba ulagi kembali " + self.name]
        else:
            print("Mermbership berhasil %s sudah selesai dilanjutkan dengan film ke %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "Sudah " + self.name + " bergabung ke membership")
            return result

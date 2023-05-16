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
            print("Kembali ke film %s; Film akan di ulang kembali!" % self.name)
            return ["Kembali ke film " + self.name]
        else:
            print("Film %s sudah selesai dilanjutkan dengan film ke %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "Film " + self.name + " sudah selesai")
            return result

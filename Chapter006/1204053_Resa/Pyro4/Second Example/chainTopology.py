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
            print("bandros kembali ke halte %s; Silahkan pesan sesuai rute yang diinginkan!" % self.name)
            return ["Bandros Segera Berangkat" + self.name]
        else:
            print("Bandros %s telah sampai ke rute selanjutnya %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "Bandros" + self.name + " sudah sampai!")
            return result

import Pyro4

@Pyro4.expose
class FileServer(object):
    def _init_(self):
        pass
    
    def send_file(self, filename):
        with open(filename, 'rb') as file:
            content = file.read()
        return content

daemon = Pyro4.Daemon()
uri = daemon.register(FileServer)
print("Server URI:", uri)

daemon.requestLoop()

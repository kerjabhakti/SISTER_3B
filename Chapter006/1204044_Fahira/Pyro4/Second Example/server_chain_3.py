from __future__ import print_function
import Pyro4
import chainTopology

current_server = "3"
next_server = "4"

servername = "example.chainTopology." + current_server

daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain(current_server, next_server)
uri = daemon.register(obj)
ns = Pyro4.locateNS()
ns.register(servername, uri)

# enter the service loop.
print("Buku %s mulai dibaca " % current_server)
daemon.requestLoop()

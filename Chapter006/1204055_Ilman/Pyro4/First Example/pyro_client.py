import Pyro4

# uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Ingin memesan tiket untuk film apa? ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))





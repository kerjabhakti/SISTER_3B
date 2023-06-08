import Pyro4

name = input("Tugas apa yang ingin anda kumpulkan? ").strip()

server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))
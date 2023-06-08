import Pyro4

name = input("Masukkan nama Anda: ").strip()
server = Pyro4.Proxy("PYRONAME:server")

print(server.welcomeMessage(name))

menu = input("Masukkan menu yang ingin dipesan: ").strip()
quantity = input("Masukkan jumlah pesanan: ").strip()

print(server.placeOrder(menu, quantity))

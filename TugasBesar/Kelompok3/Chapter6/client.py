import socket

def main():
    # Membuat socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9000)
    client_socket.connect(server_address)

    while True:
        item = input('Item: ')
        price = float(input('Price: '))
        quantity = int(input('Quantity: '))

        # Mengirim data ke server
        data = '{},{},{}'.format(item, price, quantity)
        client_socket.send(data.encode())

        # Menerima hasil dari server
        total_price = client_socket.recv(1024).decode()
        print('Total Price:', total_price)

        choice = input('Continue? (y/n): ')
        if choice.lower() != 'y':
            break

    # Menutup koneksi
    client_socket.close()

if __name__ == '__main__':
    main()

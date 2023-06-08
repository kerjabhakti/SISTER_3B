import socket

# Fungsi yang akan dijalankan pada server
def process_sale(item, price, quantity):
    total_price = price * quantity
    return total_price

def main():
    # Membuat socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9000)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print('Server running on {}:{}'.format(server_address[0], server_address[1]))

    while True:
        print('Waiting for connection...')
        client_socket, client_address = server_socket.accept()
        print('Connected from:', client_address)

        try:
            while True:
                # Menerima data dari client
                data = client_socket.recv(1024).decode()
                if not data:
                    break

                # Parsing data dari client
                sale_data = data.split(',')
                item = sale_data[0]
                price = float(sale_data[1])
                quantity = int(sale_data[2])

                # Memproses penjualan
                total_price = process_sale(item, price, quantity)

                # Mengirim hasil kembali ke client
                client_socket.send(str(total_price).encode())

        finally:
            # Menutup koneksi
            client_socket.close()

if __name__ == '__main__':
    main()

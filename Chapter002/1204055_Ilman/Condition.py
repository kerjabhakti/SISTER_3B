import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

seats = []
condition = threading.Condition()


class Customer(threading.Thread):
    def __init__(self, customer_name, seat_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_name = customer_name
        self.seat_number = seat_number

    def reserve_seat(self):
        with condition:
            # Jika seat sudah dipesan pelanggan lain maka jalankan kondisi pertama
            if self.seat_number in seats:
                logging.info('Maaf {}, Kursi {} sudah dipesan oleh pelanggan lain'.format(self.customer_name, self.seat_number))
                condition.wait()
            # Jika kursi tersedia, sistem akan menambahkan pelanggan yang memesan nomor kursi yang dipesan 
            else:
                seats.append(self.seat_number)
                logging.info('Berhasil memesan kursi untuk {} dengan nomor kursi {}'.format(self.customer_name, self.seat_number))
                condition.notify()

    def run(self):
        time.sleep(0.5)
        self.reserve_seat()


class CinemaHall:
    def __init__(self, hall_capacity):
        self.hall_capacity = hall_capacity
        self.seat_numbers = range(1, hall_capacity + 1)

    def show_available_seats(self):
        available_seats = [str(seat_number) for seat_number in self.seat_numbers if seat_number not in seats]
        logging.info('Kursi yang tersedia: {}'.format(','.join(available_seats)))


def main():
    cinema_hall = CinemaHall(10)

    customers = [
        Customer('Balmond', 2),
        Customer('Unang', 6),
        Customer('Dandi', 9),
        Customer('Saep', 5),
        Customer('Angela', 8),
        Customer('Mang Nana', 2)
        
    ]

    for customer in customers:
        customer.start()

    for customer in customers:
        customer.join()

    cinema_hall.show_available_seats()


if __name__ == "__main__":
    main()

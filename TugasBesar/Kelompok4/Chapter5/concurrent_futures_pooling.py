import concurrent.futures
import time

employee_list = ["John", "Jane", "Alice", "Bob", "Eve"]

def record_attendance(employee):
    # Simulate attendance recording process
    time.sleep(1)
    print(f"Recorded attendance for {employee}")

def verify_order():
    # Mengonfirmasi pesanan
    print("Verifikasi Pesanan:")
    print("1. Spesifikasi Mobil: ...")
    print("2. Opsi Pembayaran: ...")
    print("3. Informasi Kontak: ...")
    
    confirmation = input("Apakah Anda ingin mengkonfirmasi pesanan? (Y/N): ")

    if confirmation.upper() == "Y":
        # Mengkonfirmasi pesanan
        order_number = generate_order_number()
        print("Pesanan Anda telah dikonfirmasi.")
        print(f"Nomor Pesanan: {order_number}")
    else:
        print("Pesanan Anda dibatalkan.")

def generate_order_number():
    # Menghasilkan nomor pesanan secara acak
    return "ORD123456789"

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for employee in employee_list:
        record_attendance(employee)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(record_attendance, employee_list)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(record_attendance, employee_list)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    verify_order()

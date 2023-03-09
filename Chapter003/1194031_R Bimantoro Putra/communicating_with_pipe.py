import multiprocessing
  
def admin(conn, events):
    for event in events:
        conn.send(event)
        print(f"Bapak kost mengecheck informasi: ada {event}")
  
def user(conn):
    while True:
        event = conn.recv()
        if event == "tolak": 
            print("Anggota diterima")    
            return
        print(f"List Pembayaran : {event} Telah membayar ")
  


if __name__ == "__main__":
    events = ["kucing", "kambing", "sapi", "kelinci", "ayam"]
    conn1, conn2 = multiprocessing.Pipe()
    process_1 = multiprocessing.Process(target=admin, args=(conn1, events))
    process_2 = multiprocessing.Process(target=user, args=(conn2,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
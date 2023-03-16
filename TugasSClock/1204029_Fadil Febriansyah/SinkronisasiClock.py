import datetime
import requests

def get_server_time():
    response = requests.head('https://www.kaggle.com')
    server_time_str = response.headers['date']
    server_time = datetime.datetime.strptime(server_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    return server_time

def sync_clock():
    # Lakukan sinkronisasi menggunakan algoritma Cristian
    server_time = get_server_time()
    local_time = datetime.datetime.now()
    time_difference = server_time - local_time
    christian_synced_time = datetime.datetime.now() + time_difference
    
    # Lakukan sinkronisasi menggunakan algoritma Berkley
    n_servers = 1 # Jumlah server yang digunakan 
    offset_sum = time_difference.total_seconds()
    for i in range(n_servers - 1):
        server_time = get_server_time()
        offset = (server_time - christian_synced_time).total_seconds()
        offset_sum += offset
    offset_avg = offset_sum / n_servers
    synced_time = christian_synced_time + datetime.timedelta(seconds=offset_avg)
    
    return christian_synced_time, synced_time

# Tampilkan waktu lokal
local_time = datetime.datetime.now()
print("Waktu lokal: ", local_time)

# Tampilkan waktu server
server_time = get_server_time()
print("Waktu server: ", server_time)

# Tampilkan waktu yang sudah disinkronisasi (Cristian dan Berkley)
christian_synced_time, synced_time = sync_clock()
print("Waktu yang disinkronisasi (Cristian): ", christian_synced_time)
print("Waktu yang disinkronisasi (Berkley): ", synced_time)

if __name__ == '__main__':
    get_server_time()
    sync_clock()

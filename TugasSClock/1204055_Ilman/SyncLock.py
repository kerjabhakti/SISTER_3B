import requests
import datetime
import time

# request ke youtube
def synchronize_with_web():
    url = 'http://www.youtube.com/'
    response = requests.get(url, verify=True)
    date_str = response.headers['date']
# Pengambilan tanggal dengan format tanggal dan jam
    date_obj = datetime.datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    server_time = date_obj.timestamp()
    return server_time

if __name__ == '__main__':
    # Menyinkronkan waktu dengan web
    server_time = synchronize_with_web()
    local_time = time.time()
    time_offset = server_time - local_time
    
    # Menghitung waktu lokal yang disinkronkan dengan waktu server
    synced_time = time.time() + time_offset
    
    # Mencetak waktu dari masing-masing waktu yang ada
    print(f'Waktu lokal: {datetime.datetime.fromtimestamp(local_time)}')
    print(f'Waktu server youtube: {datetime.datetime.fromtimestamp(server_time)}')
    print(f'Waktu yang di-sinkron dengan web: {datetime.datetime.fromtimestamp(synced_time)}')
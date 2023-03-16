# Algoritma Barkeley merupakan sebuah algoritma untuk menjaga sinkronisasi waktu antara beberapa komputer dalam sebuah jaringan.

import requests
import datetime
import time

def synchronize_with_web():
    url = 'https://www.youtube.com/'
    response = requests.get(url, verify=True)
    date_str = response.headers['date']
    date_obj = datetime.datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    return date_obj.timestamp()

def calculate_offset(rtt_list):
    sorted_rtt_list = sorted(rtt_list)
    median_rtt = sorted_rtt_list[len(sorted_rtt_list) // 2]
    return median_rtt / 2

def barkeley_sync():
    # Mendapatkan waktu lokal sebelum disinkronkan
    local_time_before_sync = time.time()

    # Mendapatkan waktu dari masing-masing client
    client_times = [local_time_before_sync] * 5
    for i in range(len(client_times)):
        client_times[i] = synchronize_with_web()

    # Menghitung RTT (Round-Trip Time)
    rtt_list = []
    for i in range(len(client_times)):
        rtt = client_times[i] - local_time_before_sync
        rtt_list.append(rtt)

    # Menghitung offset
    offset = calculate_offset(rtt_list)

    # Menyinkronkan waktu lokal dengan offset yang dihitung
    local_time_after_sync = time.time() + offset

    # Mencetak waktu dari masing-masing waktu yang ada
    print(f'Waktu lokal sebelum di-sinkron: {datetime.datetime.fromtimestamp(local_time_before_sync)}')
    for i in range(len(client_times)):
        print(f'Waktu {i+1} client: {datetime.datetime.fromtimestamp(client_times[i])}')
    print(f'Waktu lokal sesudah di-sinkron: {datetime.datetime.fromtimestamp(local_time_after_sync)}')

if __name__ == '__main__':
    barkeley_sync()
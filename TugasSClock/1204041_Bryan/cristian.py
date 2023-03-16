import requests
import datetime

# Ambil waktu dari website
response = requests.get('http://www.youtube.com')
server_time = response.headers['Date']

# Konversi waktu dari string menjadi datetime object
server_time = datetime.datetime.strptime(server_time, '%a, %d %b %Y %H:%M:%S %Z')

# Hitung perbedaan waktu antara laptop dengan website
local_time = datetime.datetime.now()
time_diff = server_time - local_time

# Hitung waktu jeda menggunakan algoritma Christian
offset = (time_diff.total_seconds() + 0.5) // 1

# Sesuaikan waktu lokal dengan offset
local_time += datetime.timedelta(seconds=offset)

# Tampilkan hasil sinkronisasi waktu
print(f'Waktu laptop: {datetime.datetime.now()}')
print(f'Waktu server: {server_time}')
print(f'Perbandingan Waktu: {offset}')
print(f'Waktu sinkronisasi: {local_time}')
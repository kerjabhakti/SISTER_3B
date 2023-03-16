import time
import urllib.request as req

# hitung selisih waktu url dan local system
def web_local_difference(url):  
    response = req.urlopen(url)
    web_time = response.headers['Date']
    web_time = time.strptime(web_time, '%a, %d %b %Y %H:%M:%S %Z')
    web_time_seconds = time.mktime(web_time)
    local_time_seconds = time.time()
    return web_time_seconds - local_time_seconds, web_time

# sinkronisasi waktu web dan waktu local system menggunakan algoritma berkeley
def synchronize_web_local_time(url):
    # ambil waktu local system satuan detik
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    print('Waktu lokal:', local_time)

    # ambil waktu web satuan detik
    web_time_difference, web_time = web_local_difference(url)
    print('Waktu web:', time.strftime("%a, %d %b %Y %H:%M:%S %Z", web_time))

    # ambil selisih waktu dari tiap mesin
    time_differences = []
    for i in range(9):
        time_difference, _ = web_local_difference(url)
        time_differences.append(time_difference)

    # itung rata2 selisih waktu satuan detik
    avg_time_difference = sum(time_differences) / len(time_differences)
    print('Rata-Rata Selisih waktu:', avg_time_difference,' detik')

    # sinkronisasi waktu mesin dengan rata2 selisih
    for i in range(9):
        corrected_time = time.time() + (avg_time_difference - time_differences[i])
        print('Waktu mesin',i+1,'yang disesuaikan:', time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime(corrected_time)))

if __name__ == '__main__':
    url = 'https://www.denjandmuammar.space'
    synchronize_web_local_time(url)
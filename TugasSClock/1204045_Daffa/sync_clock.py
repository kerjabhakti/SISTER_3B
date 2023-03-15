import time
import urllib.request

def get_time_difference(url):
    """
    Mengembalikan selisih waktu antara server web publik dan sistem lokal dalam detik.
    """
    response = urllib.request.urlopen(url)
    web_time = response.headers['Date']
    web_time = time.strptime(web_time, '%a, %d %b %Y %H:%M:%S %Z')
    web_time_in_seconds = time.mktime(web_time)
    local_time_in_seconds = time.time()
    return web_time_in_seconds - local_time_in_seconds, web_time

def synchronize_time(url):
    """
    Menyesuaikan waktu sistem lokal dengan waktu server web publik menggunakan algoritma Cristian.
    """
    # Mendapatkan waktu lokal
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    print(f'Waktu lokal: {local_time}')

    # Mendapatkan waktu web publik
    web_time_difference, web_time = get_time_difference(url)
    print(f'Waktu web publik: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", web_time)}')

    # Mendapatkan waktu respon pertama dari server
    t1 = time.time()
    response = urllib.request.urlopen(url)
    t2 = time.time()
    web_time = response.headers['Date']
    web_time = time.strptime(web_time, '%a, %d %b %Y %H:%M:%S %Z')
    web_time_in_seconds = time.mktime(web_time)
    
    # Menghitung waktu yang diperlukan untuk menerima respons server
    response_time = (t2 - t1) / 2
    
    # Menghitung waktu koreksi
    time_correction = web_time_in_seconds + response_time - time.time()
    
    # Menyesuaikan waktu lokal dengan waktu server
    corrected_time = time.time() + time_correction
    print(f'Waktu mesin yang disesuaikan: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime(corrected_time))}')

if __name__ == '__main__':
    url = 'http://www.github.com'
    synchronize_time(url)

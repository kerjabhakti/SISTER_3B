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
    Menyesuaikan waktu sistem lokal dengan waktu server web publik menggunakan algoritma Berkeley.
    """
    # Mendapatkan waktu lokal
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    print(f'Waktu lokal: {local_time}')

    # Mendapatkan waktu web publik
    web_time_difference, web_time = get_time_difference(url)
    print(f'Waktu web publik: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", web_time)}')

    # Mendapatkan selisih waktu dari setiap mesin
    time_differences = []
    for i in range(3):
        time_difference, _ = get_time_difference(url)
        time_differences.append(time_difference)

    # Menghitung rata-rata selisih waktu
    avg_time_difference = sum(time_differences) / len(time_differences)
    print(f'Selisih waktu: {avg_time_difference} detik')

    # Menyesuaikan waktu setiap mesin dengan rata-rata selisih waktu
    for i in range(3):
        corrected_time = time.time() + (avg_time_difference - time_differences[i])
        print(f'Waktu mesin {i+1} yang disesuaikan: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime(corrected_time))}')

if __name__ == '__main__':
    url = 'http://www.facebook.com'
    synchronize_time(url)


# Pada codingan di atas, algoritma yang digunakan adalah algoritma Berkeley. Hal ini dapat dilihat dari langkah-langkah yang dilakukan, yaitu:

# Mendapatkan waktu lokal dan waktu web publik
# Mendapatkan selisih waktu dari setiap mesin dengan web publik
# Menghitung rata-rata selisih waktu
# Menyesuaikan waktu setiap mesin dengan rata-rata selisih waktu
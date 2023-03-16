import time
import requests

def get_time_difference(url):
    # Mendapatkan selisih waktu antara server web publik dan sistem lokal dalam detik.
    response = requests.head(url, allow_redirects=True)
    web_time = response.headers.get('date')
    web_time = time.strptime(web_time, '%a, %d %b %Y %H:%M:%S %Z')
    web_time_in_seconds = time.mktime(web_time)
    local_time_in_seconds = time.time()
    return web_time_in_seconds - local_time_in_seconds

def synchronize_time(url):
    # Menyesuaikan waktu sistem lokal dengan waktu server web publik Shopee menggunakan algoritma Berkeley.
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    print(f'Waktu lokal: {local_time}')

    web_time_difference = get_time_difference(url)
    web_time = time.localtime(time.time() + web_time_difference)
    print(f'Waktu server Shopee: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", web_time)}')

    time_differences = []
    for i in range(3):
        time_difference = get_time_difference(url)
        time_differences.append(time_difference)

    avg_time_difference = sum(time_differences) / len(time_differences)
    print(f'Selisih waktu: {avg_time_difference} detik')

    for i in range(3):
        corrected_time = time.time() + (avg_time_difference - time_differences[i])
        print(f'Waktu mesin {i+1} yang disesuaikan: {time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime(corrected_time))}')

if __name__ == '__main__':
    url = 'https://shopee.co.id'
    synchronize_time(url)

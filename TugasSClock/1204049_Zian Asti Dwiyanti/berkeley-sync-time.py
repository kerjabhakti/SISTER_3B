import datetime
import urllib.request

def get_time_from_server(server_url):
    """ Mengambil waktu dari server. """
    try:
        response = urllib.request.urlopen(server_url)
        time_str = response.headers['Date']
        server_time = datetime.datetime.strptime(time_str, '%a, %d %b %Y %H:%M:%S %Z')
        return server_time.timestamp()
    except Exception as e:
        print("Gagal mengambil waktu dari server: ", e)
        return None

def berkeley_algorithm(t1, t2, t3, t4):
    """ Implementasi algoritma Berkeley untuk sinkronisasi waktu. """
    return ((t2 - t1) + (t3 - t4)) / 2

if __name__ == "__main__":
    # Ambil waktu lokal pada laptop
    local_time = datetime.datetime.now().timestamp()

    # Sinkronisasi waktu dengan server dicoding.com
    server_url = 'https://www.dicoding.com/'
    server_time = get_time_from_server(server_url)

    if server_time is not None:
        # Hitung selisih waktu dan sinkronisasi waktu
        delta_time = berkeley_algorithm(local_time, server_time, local_time, datetime.datetime.now().timestamp())
        synced_time = local_time + delta_time

        # Tampilkan hasil sinkronisasi waktu
        print("Waktu lokal pada laptop: ", datetime.datetime.fromtimestamp(local_time))
        print("Waktu server dicoding.com: ", datetime.datetime.fromtimestamp(server_time))
        print("Selisih waktu: ", delta_time)
        print("Sinkronisasi waktu: ", datetime.datetime.fromtimestamp(synced_time))

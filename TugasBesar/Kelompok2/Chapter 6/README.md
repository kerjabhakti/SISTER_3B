# Pyro4 Game Server

Ini adalah program sederhana yang menggunakan Pyro4 untuk membangun server game dengan komunikasi jarak jauh. Server menyambut pemain dengan pesan selamat datang dan mengizinkan pemain untuk memasukkan nickname mereka. Server ini berjalan sebagai daemon dan didaftarkan di Pyro name server untuk diakses oleh client.
Program ini merupakan contoh penggunaan Pyro4 untuk komunikasi antarproses menggunakan Remote Procedure Call (RPC). Program terdiri dari dua file:

1. `pyro_client.py`: File ini digunakan untuk menjalankan client yang akan terhubung ke server Pyro4.
2. `pyro_server.py`: File ini berisi implementasi server Pyro4 yang akan menerima panggilan dari client.

## Cara Menjalankan Program

### Persiapan

Sebelum menjalankan program, pastikan Anda telah menginstal library Pyro4 dengan menggunakan perintah berikut:
```
pip install Pyro4
```

### Langkah-langkah

1. Jalankan perintah `python -m Pyro4.naming` untuk memulai name server Pyro4.

2. Jalankan file `pyro_server.py` dengan perintah `python pyro_server.py`. Server akan memulai dan terhubung ke name server Pyro4.

3. Jalankan file `pyro_client.py` dengan perintah `python pyro_client.py`. Client akan meminta Anda untuk memasukkan nickname.

4. Setelah memasukkan nickname, client akan terhubung ke server Pyro4 dan menerima pesan penyambutan dari server.

## Penjelasan Kode

### File `pyro_client.py`

```python
import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Masukkan Nickname: ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))
```

- Baris 1: Import library `Pyro4` untuk menggunakan fungsi-fungsi Pyro4.
- Baris 4: Meminta pengguna untuk memasukkan nickname.
- Baris 7: Membuat proxy Pyro4 untuk mengakses objek server yang terdaftar di name server dengan nama "server".
- Baris 8: Memanggil metode `welcomeMessage` pada objek server dengan melewatkan nickname sebagai argumen.
- Baris 9: Mencetak pesan penyambutan dari server.

### File `pyro_server.py`

```python
import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Selamat datang kembali pahlawan " + str(name))

def startServer():
    server = Server()
    # make a Pyro daemon
    daemon = Pyro4.Daemon()
    # locate the name server running
    ns = Pyro4.locateNS()
    # register the server as a Pyro object
    uri = daemon.register(server)
    # register the object with a name in the name server
    ns.register("server", uri)
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    # start the event loop of the server to wait for calls
    daemon.requestLoop()

if __name__ == "__main__":
    startServer()
```

- Baris 4-8: Mendefinisikan kelas `Server` yang akan digunakan sebagai objek Pyro4 yang dapat dipanggil dari client.
- Baris 5: Mendekorasi metode `welcomeMessage` dengan `@Pyro4.expose` agar metode ini dapat dipanggil dari luar.
- Baris 6: Metode

 `welcomeMessage` menerima satu argumen `name` yang berisi nickname dari client. Metode ini mengembalikan pesan penyambutan dengan menambahkan nickname tersebut.
- Baris 13-27: Mendefinisikan fungsi `startServer` yang akan memulai server Pyro4.
- Baris 15: Membuat objek `Server`.
- Baris 18: Membuat daemon Pyro4.
- Baris 21: Mencari name server yang berjalan.
- Baris 24: Mendaftarkan objek server sebagai objek Pyro di name server.
- Baris 26: Mencetak URI (Uniform Resource Identifier) objek server yang terdaftar.
- Baris 29: Memulai event loop server untuk menunggu panggilan dari client.

## Output

Setelah menjalankan client dengan menjalankan perintah `python pyro_client.py`, program akan meminta Anda untuk memasukkan nickname. Setelah memasukkan nickname, program akan terhubung ke server dan menerima pesan penyambutan dari server. Contoh output dapat berupa:

```
Masukkan Nickname: Hero123
Selamat datang kembali pahlawan Hero123
```

Output tersebut menunjukkan bahwa server telah menerima nickname "Hero123" dari client dan mengembalikan pesan penyambutan yang telah ditambahkan dengan nickname tersebut.

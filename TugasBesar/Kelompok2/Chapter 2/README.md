# Game Level Up

Ini adalah program sederhana yang menunjukkan peningkatan level dalam sebuah game menggunakan _threading_ di Python. Setiap level akan dieksekusi secara _concurrent_ (bersamaan) dengan bantuan _threading.Thread_.

## Cara Menjalankan Program

1. Pastikan Anda memiliki Python terinstal di komputer Anda. Anda dapat mengunduh Python dari [situs resmi Python](https://www.python.org/downloads/) dan mengikuti instruksi instalasi yang disediakan.
2. Salin kode program di atas dan simpan dalam file dengan ekstensi _.py_ (misalnya, _game_level_up.py_).
3. Buka terminal atau _command prompt_.
4. Navigasilah ke direktori tempat Anda menyimpan file _game_level_up.py_ menggunakan perintah _cd_ (misalnya, `cd C:\Path\to\file`).
5. Jalankan program dengan menjalankan perintah `python game_level_up.py`.

## Penjelasan Kode Program

```python
import threading

def game(level):
    return print('Kamu berhasil mencapai level {}'.format(level))

def main():
    threads = []
    for i in range(1, 11):
        t = threading.Thread(target=game, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
```

1. _Thread_ diimpor dari modul _threading_.
2. Fungsi `game(level)` didefinisikan. Fungsi ini akan mencetak pesan yang menunjukkan level yang berhasil dicapai.
3. Fungsi `main()` didefinisikan. Fungsi ini akan menjalankan program utama.
4. Sebuah daftar `threads` dibuat untuk menyimpan objek _thread_.
5. Melalui perulangan `for`, _thread_ dibuat sebanyak 10 kali untuk setiap level dari 1 hingga 10.
6. Setiap _thread_ akan diinisialisasi dengan `target=game` yang berarti fungsi `game()` akan dieksekusi oleh setiap _thread_, dan `args=(i,)` yang berarti argumen yang diberikan ke fungsi `game()` adalah nilai level saat ini.
7. Setiap _thread_ ditambahkan ke daftar `threads`.
8. _Thread_ dimulai dengan memanggil metode `start()` pada setiap objek _thread_.
9. _Thread_ ditunggu hingga selesai dengan memanggil metode `join()` pada setiap objek _thread_. Hal ini memastikan bahwa setiap _thread_ selesai sebelum program berakhir.

Program ini akan mencetak pesan "Kamu berhasil mencapai level [level]" untuk setiap level dari 1 hingga 10 secara _concurrent_. Setiap pesan mewakili peningkatan level yang berhasil dicapai dalam game.

Program ini menggunakan _threading_ untuk melakukan eksekusi _concurrent_ sehingga setiap _thread_ dapat menjalankan fungsi `game()` secara bersamaan.

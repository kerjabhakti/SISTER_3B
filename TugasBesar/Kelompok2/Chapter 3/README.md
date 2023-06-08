# Simulasi Masuknya Pemain ke dalam Game dengan Pemrograman Paralel

Ini adalah contoh program sederhana yang mengimplementasikan pemrograman paralel menggunakan modul `multiprocessing` di Python. Program ini menjalankan beberapa proses secara bersamaan untuk mensimulasikan game multiplayer. Setiap proses mewakili pemain dalam game.

## Penjelasan Kode

### Import Modul

```python
import multiprocessing
```

Modul `multiprocessing` digunakan untuk melakukan pemrograman paralel dengan memanfaatkan kemampuan multiprocessing pada komputer.

### Definisi Kelas `GameProcess`

```python
class GameProcess(multiprocessing.Process):
```

Kelas `GameProcess` adalah subclass dari `multiprocessing.Process`, yang digunakan untuk membuat proses baru.

#### Metode `__init__()`

```python
    def __init__(self, player_id):
        super(GameProcess, self).__init__()
        self.player_id = player_id
```

Metode `__init__()` adalah metode konstruktor yang dipanggil saat objek `GameProcess` dibuat. Metode ini menerima `player_id` sebagai argumen, yang merupakan ID unik untuk pemain. Setiap pemain akan memiliki ID yang berbeda.

#### Metode `run()`

```python
    def run(self):
        print('Player %d telah memasuki game' % self.player_id)
        return
```

Metode `run()` merupakan metode yang akan dijalankan pada proses yang baru dibuat. Dalam contoh ini, metode ini hanya mencetak pesan masuknya pemain ke dalam game dengan menggunakan ID pemain.

### Main Program

```python
if __name__ == '__main__':
    for i in range(10):
        process = GameProcess(i)
        process.start()
        process.join()
```

Bagian ini merupakan main program yang akan dijalankan saat file dieksekusi. Pada bagian ini, kita membuat 10 objek `GameProcess` dengan ID pemain yang berbeda, memulai setiap proses dengan memanggil metode `start()`, dan kemudian menunggu setiap proses selesai dengan memanggil metode `join()`.

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan kode program di atas dalam file dengan nama `game_multiplayer.py`.
3. Buka terminal atau command prompt, lalu masuk ke direktori tempat file `game_multiplayer.py` disimpan.
4. Jalankan program dengan menjalankan perintah berikut:

```
python game_multiplayer.py
```

5. Anda akan melihat output yang mencetak pesan masuknya setiap pemain ke dalam game.

**Catatan**: Output pesan masuknya pemain mungkin tidak muncul dalam urutan yang teratur, karena proses-proses berjalan secara paralel dan pesan output dapat dicetak dalam urutan yang berbeda tergantung pada penjadwalan sistem operasi.

---

Program ini memberikan contoh sederhana tentang bagaimana melakukan pemrograman paralel menggunakan modul `multiprocessing` di Python. Anda dapat mengubah dan memperluas program ini untuk menciptakan simulasi game multiplayer yang lebih kompleks atau untuk mengimplementasikan tugas-tugas pemrograman paralel lainnya.

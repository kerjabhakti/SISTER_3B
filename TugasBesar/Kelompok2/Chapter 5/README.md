## Game Battle menggunakan Asyncio

Program "Battles of Async" adalah sebuah simulasi pertarungan antara pemain dan monster menggunakan asynchronous programming dengan library `asyncio` di Python. Program ini menggambarkan sebuah pertarungan di mana pemain dan monster saling menyerang dengan kekuatan yang bergantung pada level pemain dan kekuatan monster.

### Cara Menjalankan Program

Gunakan perintah berikut untuk menjalankan program:

```
py asyncio_and_futures.py <player_level> <monster_power>
```

Contoh:

```
py asyncio_and_futures.py 15 10
```

### Penjelasan Kode

Berikut adalah penjelasan baris per baris dari kode program "Battles of Async":

```python
import asyncio
import sys
```

- Import library `asyncio` untuk melakukan asynchronous programming.
- Import library `sys` untuk mengambil argumen dari baris perintah.

```python
async def player_attack(level):
    attack = level * 5
    await asyncio.sleep(2)
    return attack
```

- Mendefinisikan fungsi `player_attack` yang merupakan asinkron. Fungsi ini menerima argumen `level` yang merupakan level pemain.
- Menghitung serangan pemain dengan mengalikan level pemain dengan 5.
- Menggunakan `await asyncio.sleep(2)` untuk mensimulasikan serangan yang membutuhkan waktu 2 detik.
- Mengembalikan nilai serangan.

```python
async def monster_attack(power):
    attack = power * 3
    await asyncio.sleep(2)
    return attack
```

- Mendefinisikan fungsi `monster_attack` yang merupakan asinkron. Fungsi ini menerima argumen `power` yang merupakan kekuatan monster.
- Menghitung serangan monster dengan mengalikan kekuatan monster dengan 3.
- Menggunakan `await asyncio.sleep(2)` untuk mensimulasikan serangan yang membutuhkan waktu 2 detik.
- Mengembalikan nilai serangan.

```python
async def battle(player_level, monster_power):
    player_task = asyncio.create_task(player_attack(player_level))
    monster_task = asyncio.create_task(monster_attack(monster_power))
    await asyncio.gather(player_task, monster_task)
    player_attack_result = player_task.result()
    monster_attack_result = monster_task.result()
    if player_attack_result > monster_attack_result:
        return 'Pemain menang! (Karena serangan sebesar %s berhasil mengalahkan serangan monster sebesar %s)' % (player_attack_result, monster_attack_result)
    elif player_attack_result < monster_attack_result:
        return 'Monster menang! (Karena serangan sebesar %s berhasil mengalahkan serangan pemain sebesar %s)' % (monster_attack_result, player_attack_result)
    else:
        return 'Pertarungan berakhir seri! (Karena serangan pemain dan monster sama kuat, yakni %s)' % player_attack_result
```

- Mendefinisikan fungsi `battle` yang merupakan asinkron. Fungsi ini menerima argumen `player_level` (level pemain) dan `monster_power` (kekuatan monster).
- Membuat task asinkron `player_task` yang akan menjalankan fungsi `player_attack` dengan level pemain sebagai argumen.
- Membuat task asinkron `monster_task` yang akan menjalankan fungsi `monster_attack` dengan kekuatan monster sebagai argumen.
- Menggunakan `await asyncio.gather

(player_task, monster_task)` untuk menunggu kedua task selesai.
- Mengambil hasil serangan pemain dan monster dari masing-masing task menggunakan `player_task.result()` dan `monster_task.result()`.
- Membandingkan hasil serangan pemain dan monster. Jika serangan pemain lebih besar, pemain menang. Jika serangan monster lebih besar, monster menang. Jika serangan pemain dan monster sama kuat, pertarungan berakhir seri.
- Mengembalikan pesan hasil pertarungan.

```python
async def main():
    player_level = int(sys.argv[1])
    monster_power = int(sys.argv[2])

    result = await battle(player_level, monster_power)
    print(result)
```

- Mendefinisikan fungsi `main` yang merupakan asinkron.
- Mengambil argumen `player_level` dan `monster_power` dari baris perintah menggunakan `sys.argv`.
- Menjalankan pertarungan dengan memanggil fungsi `battle` dengan level pemain dan kekuatan monster sebagai argumen.
- Menyimpan hasil pertarungan ke dalam variabel `result`.
- Mencetak hasil pertarungan.

```python
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```

- Memastikan bahwa program dijalankan sebagai skrip utama.
- Mendapatkan event loop menggunakan `asyncio.get_event_loop()`.
- Menjalankan fungsi `main()` secara asinkron menggunakan `loop.run_until_complete(main())`.
- Menutup event loop setelah selesai.

Dengan menjalankan program ini, Anda dapat mensimulasikan pertarungan antara pemain dan monster dengan memberikan level pemain dan kekuatan monster sebagai argumen saat menjalankan program. Hasil pertarungan akan dicetak di output.

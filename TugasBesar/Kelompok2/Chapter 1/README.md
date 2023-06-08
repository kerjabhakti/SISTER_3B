# Game RPG

Ini adalah program sederhana untuk game RPG. Program ini akan membuat sebuah file teks dengan nama 'namafilenya.txt' dan menuliskan beberapa pesan ke dalamnya. Setelah itu, program akan membaca isi file tersebut dan mencetaknya di layar.

## Instruksi

1. Pastikan Python telah terinstal di komputer Anda.
2. Buka sebuah text editor dan salin kode program di bawah ini ke dalam editor:

```python
f = open('namafilenya.txt', 'w')
f.write('Game RPG\n')
f.write('Press Start to begin adventure\n')
f.close()

f = open('namafilenya.txt')
content = f.read()
print(content)

f.close()
```

3. Simpan file dengan nama `game_rpg.py`.
4. Buka terminal atau command prompt, lalu arahkan ke direktori tempat Anda menyimpan file `game_rpg.py`.
5. Jalankan program dengan mengetikkan perintah berikut di terminal atau command prompt:

   ```shell
   python game_rpg.py
   ```

6. Program akan membuat file 'namafilenya.txt' dan menuliskan pesan di dalamnya. Kemudian, isi file akan dibaca dan ditampilkan di layar.

## Penjelasan Kode

Berikut adalah penjelasan baris per baris dari kode program:

```python
f = open('namafilenya.txt', 'w')
f.write('Game RPG\n')
f.write('Press Start to begin adventure\n')
f.close()
```

- Baris 1: Membuka file dengan nama 'namafilenya.txt' dalam mode 'w' (write) menggunakan fungsi `open()`. Jika file sudah ada, isi file sebelumnya akan dihapus. Jika file belum ada, file baru akan dibuat.
- Baris 2 dan 3: Menuliskan pesan 'Game RPG' dan 'Press Start to begin adventure' ke dalam file menggunakan metode `write()` pada objek file (`f`).
- Baris 4: Menutup file menggunakan metode `close()` pada objek file.

```python
f = open('namafilenya.txt')
content = f.read()
print(content)
f.close()
```

- Baris 6: Membuka file 'namafilenya.txt' dalam mode default ('r', read) menggunakan fungsi `open()`. File akan dibaca.
- Baris 7: Membaca isi file menggunakan metode `read()` pada objek file (`f`) dan menyimpannya ke dalam variabel `content`.
- Baris 8: Mencetak isi file (`content`) di layar.
- Baris 9: Menutup file menggunakan metode `close()` pada objek file.

## Hasil

Setelah menjalankan program, Anda akan melihat pesan-pesan berikut di layar:

```
Game RPG
Press Start to begin adventure
```

Isi file 'namafilenya.txt' juga akan sama dengan pesan-pesan di atas.

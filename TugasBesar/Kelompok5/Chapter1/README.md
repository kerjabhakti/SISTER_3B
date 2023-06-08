# Program Pemesanan Makanan

Program Pemesanan Makanan adalah sebuah program sederhana yang memodelkan proses pemesanan makanan. Program ini menggunakan kelas `Pesanan` untuk merepresentasikan pesanan makanan yang dilakukan oleh pengguna. Setiap kali sebuah pesanan dibuat, jumlah pesanan akan ditambahkan ke total pesanan secara keseluruhan.

## Fitur

- Membuat pesanan makanan dengan menyediakan nama makanan dan jumlah pesanan.
- Menampilkan informasi pesanan, termasuk nama makanan dan jumlah pesanan.
- Menampilkan total pesanan keseluruhan.

## Cara Menggunakan

1. Buat objek `Pesanan` dengan menyediakan nama makanan dan jumlah pesanan. Contoh:

```python
pesanan_1 = Pesanan("Burger", 2)
```

2. Untuk mendapatkan informasi pesanan, panggil metode `get_info()` pada objek pesanan. Contoh:

```python
print(pesanan_1.get_info())
```

Output yang dihasilkan akan menampilkan nama makanan dan jumlah pesanan.

3. Untuk mendapatkan total pesanan keseluruhan, panggil metode `get_total_pesanan()`. Contoh:

```python
print(pesanan_1.get_total_pesanan())
```

Output yang dihasilkan akan menampilkan total pesanan semua pesanan yang telah dibuat.

## Contoh Penggunaan

Berikut adalah contoh penggunaan program:

```python
# Pemesanan Makanan
pesanan_1 = Pesanan("Burger", 2)
print(pesanan_1.get_info())
print(pesanan_1.get_total_pesanan())

pesanan_2 = Pesanan("Pizza", 3)
print(pesanan_2.get_info())
print(pesanan_2.get_total_pesanan())
```

Output:

```
Pesanan: Burger
Jumlah: 2
Total Pesanan: 5
Pesanan: Pizza
Jumlah: 3
Total Pesanan: 5
```

Pada contoh di atas, dua pesanan makanan dibuat, yaitu "Burger" dengan jumlah 2 dan "Pizza" dengan jumlah 3. Setelah itu, informasi pesanan dan total pesanan keseluruhan ditampilkan.

## Kontribusi

Anda dapat berkontribusi pada pengembangan program ini dengan melakukan fork repository ini dan membuat pull request dengan perubahan yang Anda usulkan.

Jika Anda menemui masalah atau memiliki saran, silakan buat _issue_ baru di repository ini.

## Lisensi

Program ini menggunakan lisensi MIT. Silakan lihat file `LICENSE` untuk informasi lebih lanjut.

---

Terima kasih telah menggunakan Program Pemesanan Makanan. Nikmati pengalaman pemesanan makanan yang mudah dan menyenangkan! 🍔🍕

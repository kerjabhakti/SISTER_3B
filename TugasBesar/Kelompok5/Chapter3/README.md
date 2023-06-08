# Program Pemrosesan Pesanan Makanan

Program Pemrosesan Pesanan Makanan adalah sebuah program yang mengilustrasikan pemrosesan paralel dari pesanan makanan menggunakan modul `multiprocessing` dalam Python. Program ini memungkinkan pemrosesan simultan dari beberapa pesanan makanan untuk meningkatkan efisiensi dan kecepatan.

## Fitur

- Memproses pesanan makanan secara paralel menggunakan multiprocessing.
- Menangani pesanan makanan dengan metode `process_order()`.
- Menerima daftar pesanan makanan dan memprosesnya secara bersamaan.

## Cara Menggunakan

1. Definisikan fungsi `process_order(order)` untuk memproses pesanan makanan. Anda dapat mengganti kode di dalam fungsi ini sesuai dengan logika pemrosesan pesanan yang Anda inginkan.

2. Tentukan daftar pesanan makanan dalam variabel `orders`. Anda dapat menambahkan atau mengubah pesanan sesuai kebutuhan.

3. Jalankan program dengan memanggil fungsi `main()`. Program akan memproses setiap pesanan secara paralel menggunakan multiprocessing.

## Contoh Penggunaan

Berikut adalah contoh penggunaan program:

```python
import multiprocessing

def process_order(order):
    print("Memproses pesanan:", order)
    # Lakukan proses pemrosesan pesanan makanan
    # ...

def main():
    orders = ["Burger", "Pizza", "Sushi", "Noodle"]

    processes = []
    for order in orders:
        process = multiprocessing.Process(target=process_order, args=(order,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()
```

Output:

```
Memproses pesanan: Burger
Memproses pesanan: Pizza
Memproses pesanan: Sushi
Memproses pesanan: Noodle
```

Pada contoh di atas, program akan memproses pesanan makanan "Burger", "Pizza", "Sushi", dan "Noodle" secara bersamaan menggunakan multiprocessing. Setiap pesanan akan ditampilkan pesan "Memproses pesanan: [nama_pesanan]".

## Kontribusi

Anda dapat berkontribusi pada pengembangan program ini dengan melakukan fork repository ini dan membuat pull request dengan perubahan yang Anda usulkan.

Jika Anda menemui masalah atau memiliki saran, silakan buat _issue_ baru di repository ini.

---

Terima kasih telah menggunakan Program Pemrosesan Pesanan Makanan. Nikmati efisiensi dan kecepatan dalam pemrosesan pesanan makanan Anda! 🍔🍕🍣🍜

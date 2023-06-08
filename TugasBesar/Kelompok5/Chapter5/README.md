# Program Pemesanan Makanan dengan Asyncio

Program Pemesanan Makanan dengan Asyncio adalah sebuah program yang mengilustrasikan pemesanan makanan secara asinkron menggunakan modul `asyncio` dalam Python. Program ini memungkinkan pengguna untuk melakukan pemesanan makanan secara efisien dengan mengeksekusi beberapa pesanan secara paralel.

## Fitur

- Melakukan pemesanan makanan secara asinkron menggunakan asyncio.
- Menentukan jumlah pesanan makanan yang akan diproses.
- Menggunakan fungsi `order_food(order_id)` untuk mensimulasikan pemesanan makanan.
- Menampilkan hasil pemesanan makanan.

## Cara Menggunakan

1. Tentukan jumlah pesanan makanan yang akan diproses dengan menjalankan program melalui command line dan menyertakan argumen sebagai jumlah pesanan. Contoh: `python program.py 5`.

2. Definisikan fungsi `order_food(order_id)` untuk melakukan pemesanan makanan. Anda dapat mengganti logika pemesanan sesuai dengan kebutuhan.

3. Jalankan program dengan memanggil fungsi `main()`.

## Contoh Penggunaan

Berikut adalah contoh penggunaan program:

```python
import asyncio
import sys


async def order_food(order_id):
    # Simulasi pemesanan makanan
    await asyncio.sleep(2)
    return f"Order {order_id} food ordered"


async def main():
    # Menentukan jumlah pesanan makanan
    num_orders = int(sys.argv[1])

    tasks = []
    for i in range(num_orders):
        order_id = i + 1
        tasks.append(order_food(order_id))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
```

Output:

```
Order 1 food ordered
Order 2 food ordered
Order 3 food ordered
Order 4 food ordered
Order 5 food ordered
```

Pada contoh di atas, program akan memproses pemesanan makanan sebanyak 5 pesanan secara asinkron menggunakan asyncio. Setiap pesanan akan ditampilkan pesan "Order [nomor_pesanan] food ordered".

## Kontribusi

Anda dapat berkontribusi pada pengembangan program ini dengan melakukan fork repository ini dan membuat pull request dengan perubahan yang Anda usulkan.

Jika Anda menemui masalah atau memiliki saran, silakan buat _issue_ baru di repository ini.

---

Terima kasih telah menggunakan Program Pemesanan Makanan dengan Asyncio. Nikmati kemudahan dalam melakukan pemesanan makanan secara asinkron! 🍔🍕🍣🍜

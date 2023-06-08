### Dalam kode ini, adalah contoh penggunaan asyncio dalam Python untuk mengumpulkan tugas dari beberapa mahasiswa secara bersamaan dengan menggunakan async/await.

1. Pada bagian awal file melakukan import modul asyncio yang dibutuhkan, pembuatan function submit_tugas yang berisi simulasi proses pengumpulan tugas menggunakan function dari asyncio yaitu sleep selama 2 detik.

2. Pembuatan function utama (main), diawali dengan inisialisasi variabel jml_mahasiswa yang berisi inputan dari user terkait jumlah proses atau dalam hal ini mahasiswa yang akan mengumpulkan tugas.

3. Pembuatan variabel tugas untuk menjalankan function submit_tugas sebagai simulasi proses dan dilakukan sebanyak nilai jml_mahasiswa

4. Mengumpulkan hasil proses menggunakan function gather dari seluruh proses pada variabel tugas.

5. Melakukan looping atau iterasi sebanyak hasil gather dari variabel tugas.
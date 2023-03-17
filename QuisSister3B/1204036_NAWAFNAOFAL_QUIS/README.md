Program ini merupakan implementasi penggunaan threading pada Python dengan tema Pendaftaram Mahasiswa Baru. Terdapat dua fungsi yaitu daftar dan seleksi, di mana daftar berfungsi untuk mensimulasikan proses pendaftaran peserta dan seleksi untuk mensimulasikan proses seleksi peserta.

Pada awal program, dicetak waktu dimulainya program dengan format "Hari, tanggal Bulan tahun Jam:Menit:Detik". Kemudian dilakukan inisialisasi thread dan queue serta memulai thread untuk setiap peserta yang mendaftar.

Setelah semua peserta mendaftar, dilakukan penghitungan waktu dimulainya proses seleksi dengan mencatat waktu saat ini. Kemudian dilakukan pemrosesan data dari queue dalam thread seleksi. Jika ada data yang dapat diproses, maka akan dilakukan simulasi proses seleksi peserta dengan memberikan delay 3 detik. Jika peserta yang diproses adalah "Dadang", maka akan dicetak pesan bahwa peserta tersebut diterima, dan jika bukan "Dadang", maka yang akan ditampilkan/dicetak ialah mahasiswa tersebut ditolak.

Setelah seluruh data pada queue telah diproses, waktu sekarang dicatat lagi untuk menandai waktu selesainya proses seleksi. Kemudian dilakukan perhitungan selisih waktu dimulai dan selesai seleksi untuk menghitung total waktu seleksi. Terakhir, dicetak waktu dimulainya dan waktu selesainya proses seleksi, serta total waktu seleksi dengan format "Hari, tanggal Bulan tahun Jam:Menit:Detik".

Untuk menambahkan script untuk membandingkan kapan data tersebut berjalan dan berhenti, pada awal program dicetak waktu dimulainya program dengan format "Hari, tanggal Bulan tahun Jam:Menit:Detik". Kemudian dicetak waktu dimulainya proses seleksi saat dilakukan penghitungan waktu dimulainya proses seleksi dengan mencatat waktu saat ini. Setelah seluruh data pada queue telah diproses, waktu sekarang dicatat lagi untuk menandai waktu selesainya proses seleksi. Kemudian dicetak waktu dimulainya dan waktu selesainya proses seleksi, serta total waktu seleksi dengan format "Hari, tanggal Bulan tahun Jam:Menit:Detik". Dengan demikian, informasi waktu berjalan dan berhenti program serta proses seleksi telah ditambahkan pada program ini.

Untuk inisiasi sebuah object thread pada Python menggunakan threading (chapter 02) dan syncronization, pada program ini telah dilakukan inisialisasi thread dan queue serta penggunaan threading untuk setiap peserta yang mendaftar dan penggunaan thread untuk seleksi. Pada thread seleksi, digunakan pengkondisian untuk memastikan bahwa pemrosesan data dari queue dilakukan secara bergantian dan tidak ada dua thread yang memproses data yang sama. Hal ini dilakukan dengan memastikan bahwa jika suatu thread sedang memproses data dari queue, thread lain akan menunggu sampai proses pemrosesan selesai. Dengan demikian, penggunaan synchronization telah terpenuhi pada program ini.

Untuk urutan prosesnya, pada program ini urutan prosesnya adalah sebagai berikut:

1. Inisialisasi thread dan queue serta memulai thread untuk setiap peserta yang mendaftar.
2. Penghitungan waktu dimulainya proses seleksi.
3. Pemrosesan data dari queue dalam thread seleksi.
4. Perhitungan selisih waktu dimulai dan selesai seleksi untuk menghitung total waktu seleksi.
5. Pencetakan waktu dimulai dan waktu selesainya proses seleksi, serta total waktu seleksi.

Dengan demikian, urutan prosesnya telah terdefinisi pada program ini.

berikut merupakan screenshoot hasil seluruh prosesnya:
![image](https://user-images.githubusercontent.com/74226869/225801935-28af0a5f-19ba-47f4-a5ce-61d5efd4dc87.png)


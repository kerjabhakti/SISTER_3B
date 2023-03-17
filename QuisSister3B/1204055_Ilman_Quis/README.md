Studi kasus yang diambil yaitu poin "Nilai" dalam kodingan akan memproses penilaian terhadap mahasiswa menggunakan threading dan sycnronization.

Terdiri dari beberapa fungsi yang dijalankan yaitu "nilai_mahasiswa" dan "jalankan thread". Fungsi "nilai_mahasiswa" memiliki tunuan untuk melakukan proses menilai mahasiswa sesuai dengan nilai yang sudah diatur dan akan menampilkan ouput keterangan proses penilaian.Sedangkan jalankan thread akan memproses setiap item dari antrian penilaian mahasiswa dari fungsi "nilai_mahasiswa". Dilakukan pendefinisian terhadap variabel "q" sebagai antrian untuk menampung data mahasiswa dan nilai.

Ketika dijalankan sistem akan menjalankan setiap proses yang sudah ditentukan dengan setiap proses yang sudah selesai dijeda selama 2 detik, dari masing-masing proses akan diberitahukan kapan proses tersebut dimulai dan selesai. Sistem akan menganggap eksekusi selesai ketika seluruh proses sudah dilakukan, sehingga akan menampilkan keterangan bahwa seluruh proses penilaian sudah selesai.

Berikut adalah tampilan ketika di eksekusi:
![image](https://user-images.githubusercontent.com/80626628/225804098-cace2275-5c7d-4b2a-abff-eb029b3e0e9c.png)

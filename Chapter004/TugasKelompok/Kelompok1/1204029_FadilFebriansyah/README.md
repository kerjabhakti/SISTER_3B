# Chapter 04 - Fadil Febriansyah

Program ini merupakan implementasi MPI atau Message Passing Interface untuk simulasi layanan GoRide pada aplikasi Gojek. Program ini terdiri dari dua proses yang masing-masing merepresentasikan pengendara dan driver.

Pada proses dengan rank 1, yaitu proses pengendara, program akan mengirimkan permintaan perjalanan ke proses pengendara dengan rank 5. Setelah permintaan diterima, pengendara akan menerima status perjalanan dari pengendara dengan rank 5.

Pada proses dengan rank 5, yaitu proses pengendara, program akan mengirimkan status perjalanan ke proses pengendara dengan rank 1. Setelah status perjalanan dikirim, pengendara akan menerima permintaan perjalanan dari pengendara dengan rank 1.

Program ini hanya sebagai simulasi sederhana dan dapat dikembangkan lebih lanjut untuk keperluan lainnya.

### Screenshot
![Alt text](../1204029_FadilFebriansyahD:/Kuliah/Semester%206/Sistem%20Tersebar/Github/SISTER_3B/Chapter004/TugasKelompok/Kelompok1/1204029_FadilFebriansyah/Hasil.jpg)


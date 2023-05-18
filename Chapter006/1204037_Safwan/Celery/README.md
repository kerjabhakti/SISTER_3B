# Celery
> Studi Kasus Game: Menampilkan Level Player

## Untuk Menjalankan File Celery Ini Instal Terlebih Dahulu RabbitMQ dan Erlang Serta library Celery 

### File `addTask_main.py`:

Penjelasan kode yaitu pertama import modul addTask dan menggunakan variabel result untuk mencetak pesan tentang peringkat akun dalam permainan Mobile Legends. Pada awalnya, modul addTask diimpor ke dalam program. Selanjutnya, terdapat pemeriksaan kondisi __name__ == '__main__' yang memeriksa apakah file ini dijalankan langsung atau diimpor sebagai modul. Jika file ini dijalankan langsung, maka blok kode di dalam kondisi tersebut akan dieksekusi. Variabel result dibuat dan diinisialisasi dengan hasil pemanggilan fungsi addTask.add("Mythic", "Honor"), di mana argumen "Mythic" dan "Honor" diberikan ke fungsi add(). Setelah pemanggilan fungsi selesai, pesan "Rank Akun Mobile Legendsmu Sekarang Adalah" dicetak bersama dengan nilai yang ada dalam variabel result. Dengan demikian, kode tersebut memperoleh peringkat akun Mobile Legends menggunakan modul addTask dan mencetak pesan yang menggambarkan peringkat akun yang diperoleh dari variabel result.

Output:
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Celery/CeleryOutput.png)



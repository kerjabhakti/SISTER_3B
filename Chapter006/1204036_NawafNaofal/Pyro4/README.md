# Pyro4
> Studi Kasus Game: Memasukkan Nickname dan Penjelajahan Dungeon

**Sebelum menjalankan file yang ada dalam folder `Pyro4` ini kita harus menjalankan perintah `python -m Pyro4.naming` terlebih dahulu untuk menjalankan server Pyro4 nya**

- First Example

1.	`pyro_client.py`:

File ini merupakan client yang menggunakan library Pyro4 untuk berkomunikasi dengan server. Pada bagian awal, baris yang di-comment `#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()` dapat digunakan untuk memasukkan URI server Pyro4 secara manual. Kemudian, pengguna diminta untuk memasukkan nickname melalui `name = input("Masukkan Nickname: ").strip()`. Selanjutnya, client menggunakan proxy Pyro4 untuk menghubungi server dengan menggunakan URI PYRONAME:server. Kemudian, client mencetak pesan selamat datang yang diterima dari server. Contoh ini bertujuan untuk menunjukkan penggunaan Pyro4 dalam komunikasi client-server.

2.	`pyro_server.py`:

File ini merupakan server yang menggunakan library Pyro4 untuk melayani permintaan dari client. Di dalam kelas Server, terdapat metode `welcomeMessage()` yang didekorasi dengan `@Pyro4.expose`. Metode ini menerima parameter name dan mengembalikan pesan selamat datang yang diikuti dengan nilai name yang diterima. Pada fungsi `startServer()`, server Pyro4 dibuat menggunakan objek Server dan sebuah daemon Pyro4. Daemon tersebut kemudian diregistrasikan dengan menggunakan name server yang telah di-locate. URI dari server diambil menggunakan `daemon.register(server)` dan di-register dalam name server dengan nama `"server"`. Setelah itu, URI server dicetak untuk digunakan pada client nanti. Akhirnya, event loop daemon dimulai menggunakan `daemon.requestLoop()`. Contoh ini bertujuan untuk menunjukkan penggunaan Pyro4 dalam membuat server Pyro4 yang menerima permintaan dari client.

Output:
![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/1e3fa3fb-adc4-43d3-ad9c-4bb048cf0b09)

- Second Example

1.	`chainTopology.py`

File ini mendefinisikan kelas Chain yang merupakan bagian dari topologi rantai (chain topology). Chain memiliki metode `__init__` untuk menginisialisasi objek, dan metode process untuk memproses pesan. Jika `current_server` belum ditentukan, objek akan membuat proxy untuk `current_server` menggunakan Pyro4. Jika nama objek `(self.name)` ada dalam pesan, maka proses penjelajahan selesai dan mengembalikan pesan `"Selesei pada [nama]"`. Jika tidak, objek akan meneruskan pesan ke `current_server` untuk diproses.

2.	`client_chain.py`

File ini adalah file client yang menggunakan Pyro4 untuk terhubung ke server dengan nama `example.chainTopology.1.` Kemudian, objek obj memanggil metode process dengan pesan `"hai"` sebagai argumen, dan mencetak hasilnya.

3.	`server_chain_1.py`

File ini adalah file server yang menggunakan Pyro4 untuk membuat objek Chain dengan nama server `"example.chainTopology.1".` Objek tersebut didaftarkan ke name server dan memulai daemon untuk menerima panggilan.

4.	`server_chain_2.py`

File ini adalah file server yang serupa dengan `server_chain_1.py`, tetapi dengan nama server `"example.chainTopology.2"` dan `next_server` yang berbeda.

5.	`server_chain_3.py`

File ini adalah file server yang serupa dengan `server_chain_1.py`, tetapi dengan nama server `"example.chainTopology.3"` dan next_server yang berbeda.
File-file ini membentuk topologi rantai dengan tiga server yang saling terhubung. Ketika client `(client_chain.py)` mengirim pesan, pesan tersebut akan diproses oleh objek Chain di setiap server dalam urutan yang ditentukan.

Output:
![image](https://github.com/nawafnaofal/SISTER_3B_KELOMPOK2/assets/74226869/a37524fb-fb1a-4c0f-84ef-3251589853a5)

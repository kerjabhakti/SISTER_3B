# Pyro4
> Studi Kasus Game: Joki Tier akun Mobile Legends

Dalam file "chainTopology.py", terdapat definisi kelas bernama Chain yang memiliki metode process. Metode ini bertanggung jawab untuk memproses pesan dalam suatu rantai topologi. Setiap objek Chain memiliki atribut berupa nama dan nama server saat ini. Selain itu, objek juga memiliki kemampuan untuk memanggil metode process pada server berikutnya dalam rantai.

File "client_chain.py" berfungsi sebagai klien yang berinteraksi dengan objek Chain. Di dalamnya, kita menggunakan Pyro4 untuk membuat proxy ke objek Chain dan memanggil metode process dengan memberikan pesan sebagai argumen.

Sementara itu, file "server_chain_1.py", "server_chain_2.py", dan "server_chain_3.py" berperan sebagai server dalam rantai topologi. Setiap server akan membuat objek Chain dengan mengatur server saat ini dan server berikutnya dalam rantai. Objek tersebut akan didaftarkan di name server Pyro menggunakan Pyro4. Setelah itu, server akan memasuki loop permintaan untuk menerima panggilan dari klien.

Dengan demikian, keseluruhan file-file tersebut bekerja bersama untuk membentuk sebuah rantai topologi, di mana objek Chain diproses melalui metode process yang diperoleh dari server berikutnya dalam rantai. Klien dapat berinteraksi dengan rantai ini melalui file "client_chain.py" dengan menggunakan Pyro4.

## Output Program

### Menjalankan Pyro4 Server
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/PyroServer.png)


### First Example

#### Client
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/FirstExample/FirstExample.png)

#### Server
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/FirstExample/PyroServerFirst.png)

### Second Example

#### Server 1
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/SecondExample/Server1.png)

#### Server 2
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/SecondExample/Server2.png)

#### Server 3
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/SecondExample/Server3.png)


### Menjalankan File Client
![image](https://raw.githubusercontent.com/safwansheamus/AssetBuatNugas/main/Sister_Chapter_6/Pyro4/SecondExample/ChainClient.png)

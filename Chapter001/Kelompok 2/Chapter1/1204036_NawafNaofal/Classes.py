#induk
class tokoonline:
    pembeli = 5
    toko = 5
    name1 = 'nawaf'
    name2 = 'naofal'
    name3 = 'ujang'
    name4 = 'saepudin'

    def __init__ (self):
        self.myvariable = 8
    def myfunction (self, arg1, arg2):
        return self.myvariable

transaksi = tokoonline()
print("Toko Online Mang Dadang")
    
print("Jumlah pembeli di toko Mang Dadang", transaksi.pembeli)
print("Toko Online")

print("nama : ", transaksi.name1)

print("nama : ", transaksi.name2)

print("nama : ", transaksi.name3)

print("nama : " , transaksi.name4)
    
class KelasLain (tokoonline):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = KelasLain ("Selamat Datang Di Toko Online")
print("Silahkan pilih barang yang diinginkan " )

diskon ='Hari ini sedang ada diskon diseluruh produk sebesar 40%'
print("Kalo beli dapat " ,diskon)
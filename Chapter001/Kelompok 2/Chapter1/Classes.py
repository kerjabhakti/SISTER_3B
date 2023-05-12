#induk
class kontrakan:
    anggota = 7
    kamar = 7
    nama1 = 'matt'
    nama2 = 'bima'
    nama3 = 'nawaf'
    nama4 = 'naon'
    nama5 = 'sia'
    nama6 = 'eta'

    def __init__ (self):
        self.myvariable = 8
    def myfunction (self, arg1, arg2):
        return self.myvariable

kasus = kontrakan()
print("Kontrakan SKUY LIVING")

print("Jumlah anggota kontrakan ",kasus.anggota)
print("Jumlah kamar ",kasus.kamar)


print("nama : ", kasus.nama1)

print("nama : ", kasus.nama2)

print("nama : ", kasus.nama3)

print("nama : " , kasus.nama4)

#kontrakan.nama5 = 'lol'

print("nama : ", kasus.nama5)
print("nama : ", kasus.nama6)
#anak class
class AnotherClass (kontrakan):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("Selamat Datang Di Kontrakan")
print("Join kontrakan yuksssss " )

Join_yuks ='Free WIFI'
print("Kalo join dapat " ,Join_yuks)

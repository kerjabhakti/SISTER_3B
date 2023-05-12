#Program ini adalah contoh penggunaan type data yaitu list, tuple dan dictionary

#terdapat sebuah  list yang isinya : int, list, dan tuple
example = [1, ["another", "list"], ("a", "tuple")]
example


#dibawah ini terdapat list yang isinya : string, int, dan float
mylist = ["element 1", 2, 3.14]
mylist

#untuk mengubah elemen list 0
mylist[0] = "yet element 1"
print(mylist[0])

#untuk mengubah elemen list -1
mylist[-1] = 3.15
print (mylist[-1])

# dibawah ini merupakan contoh dictionary yang memiliki 3 pasang kunci-nilai.
mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}
print(mydict)

#memperbarui nilai float kunci pi menjadi 3.15
mydict["pi"] = 3.15
print(mydict["pi"])

#contoh tuple
mytuple = (1, 2, 3)
print(mytuple)

# variabel yang menyimpan method len() yang digunakan untuk menghitung panjang list atau str.
myfunc = len
print (myfunc(mylist))
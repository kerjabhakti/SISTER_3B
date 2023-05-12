import random
# Melakukan perhitungan dasar, termasuk membangun sebuah daftar bilangan bulat secara acak. 
# Fungsi ini akan digunakan dalam sebuah program Python yang bertujuan untuk membandingkan waktu eksekusi 
# dari tiga skenario yaitu serial, multithread, dan multiprocess.

def do_something(count,out_list):
	for i in range(count):
		out_list.append(random.random())


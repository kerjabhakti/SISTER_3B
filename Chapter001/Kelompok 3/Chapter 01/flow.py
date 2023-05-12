# IF

# Program ini merupakan percabangan if-else 
# untuk mengecek apakah suatu bilangan bernilai positif, nol(zero) atau negatif

num = 1
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# FOR
# Program ini digunakan untuk menjumlahkan semua elemen yang ada pada variabel 'numbers'
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum = 0
for val in numbers:
	sum = sum+val

print("The sum is", sum)


#WHILE
# Program ini digunakan untuk menghitung jumlah bilangan bulat dari 1 hingga n (sum = 1+2+3+...+n)

n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
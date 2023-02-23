#  IF

# In this program, we check if the number is positive or negative or cer and
# display in appropriate message

# IF

# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message

# Codingan untuk melakukan pengondisian If elif
# jika num lebih dari 0 maka tampil "Positive Number"
# jika num sama dengan 0 maka tampil "Zero"
# jika dua duanya salah maka tampil "Negative Number"

num = 1
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Perulangan dimana value pada variable sum akan ditambahkan oleh
# variable val yang diisikan oleh angka yang berasal dari variabel numbers

# FOR
# Program to find the sum of all numbers stored in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

# Perulangan untuk menjumlahkan seluruh bilangan bulat
# yang dimulai dari angka satu hingga n. Variabel n bernilai 10
# hingga akan menjumlahkan seluruh bilangan dari 1 hinggan 10

#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
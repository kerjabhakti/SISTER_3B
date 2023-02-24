# Dalam program ini, 
# kami memeriksa apakah angkanya positif atau negatif atau nol dan
# tampilkan pesan yang sesuai

num = 1

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Angka Positif")
elif num == 0:
    print("Nilai Nol")
else:
    print("Angka Negatif")



# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [10, 6, 3, 8, -3, 2, 5, 44, 12]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 87
print("Nilai output :", sum)
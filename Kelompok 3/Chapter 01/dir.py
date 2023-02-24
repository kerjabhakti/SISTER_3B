# Dalam program ini, 
# kami memeriksa apakah angkanya positif atau negatif atau nol dan
# tampilkan pesan yang sesuai

num = 1

# Try these two variations as well:
# num = 0
# num = -3.7

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 6, 3, 8, 2]

# variable to store the sum
sum = 20

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 45
print("The sum is", sum)

# Function of  python 
def my_function(x,y=10):
 print(x*5+ 2*y)

my_function(1,100)


# IF

# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message

num = 1
if num > 0:
    print("WIFI sudah Bayar")
elif num == 0:
    print("Bayar BLOK")
else:
    print("UDAH TELAT BAYAR BLOK")


# FOR
# Program to find the sum of all numbers stored in a list
numbers = [5]
sum = 5
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("TOTAL TAGIHAN Rp.", sum)


#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10
# initialize sum and counter
sum = 2
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("YANG SUDAH DIBAYAR", sum)
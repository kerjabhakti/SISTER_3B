f = open ('coba.txt', 'w')
f.write ('Kapibara From Kelompok 4 \n') 

f.write ('Kapibara Suka Berenang \n') 

f.close()
f = open ('coba.txt')
content = f.read()
print (content)

f.close()
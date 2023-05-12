f = open ('Kelompok 4/Chapter 1/coba.txt', 'w')
f.write ('Kapibara Suka adalah MasBro \n') 

f.write ('Kapibara Suka Berenang \n') 

f.close()
f = open ('Kelompok 4/Chapter 1/coba.txt')
content = f.read()
print (content)

f.close()
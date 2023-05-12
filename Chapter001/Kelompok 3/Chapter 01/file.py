f = open ('test.txt', 'w')
f.write ('Kami dari kelompok 3 \n') 

f.write ('Anggotanya ada : Fahira, resa, dan zian \n') 

f.close()
f = open ('test.txt')
content = f.read()
print (content)

f.close()

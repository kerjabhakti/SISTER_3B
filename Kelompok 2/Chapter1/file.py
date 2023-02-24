f = open ('kontrakan.txt', 'w')
f.write ('Selamat datang dikontrakan SKUY LIVING \n') 

f.write ('Masuk kontrakan SKUY LIVING free WIFI \n') 

f.close()
f = open ('kontrakan.txt')
content = f.read()
print (content)

f.close()
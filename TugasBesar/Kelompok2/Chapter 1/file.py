f = open ('namafilenya.txt', 'w')
f.write ('Game RPG \n') 

f.write ('Press Start to begin adventure \n') 

f.close()
f = open ('namafilenya.txt')
content = f.read()
print (content)

f.close()

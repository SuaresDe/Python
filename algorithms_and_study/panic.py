frase = "Don't panic!"
flist = list(frase)
print(frase)
print(flist)
for i in range(4):
    flist.pop()
flist.pop(0)
flist.remove("'")
flist.extend([flist.pop(), flist.pop()])
flist.insert(2, flist.pop(3))
nova_frase = ''.join(flist)
print(flist)
print(nova_frase)
frase = "Don't panic!"
flist = list(frase)
print(frase)
print(flist)
nova_frase = ''.join(flist[1:3])
nova_frase = nova_frase + ''.join([flist[5], flist[4], flist[7], flist[6]])
print(flist)
print(nova_frase)
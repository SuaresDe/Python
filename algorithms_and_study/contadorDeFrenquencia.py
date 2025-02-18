vogais = ['a','e','i','o','u']
palavra = input("Insira uma palavra pra procurar pelas vogais: ")

encontrado = {}

encontrado['a'] = 0
encontrado['e'] = 0
encontrado['i'] = 0
encontrado['o'] = 0
encontrado['u'] = 0

for letras in palavra:
    if letras in vogais:
        encontrado[letras] += 1

for k,v in sorted(encontrado.items()):
    print( k, "foi encontrado", v,"vezes.")
vogais = {'a','e','e','i','o','u','u'}

vogais2 = set('aeeioouu')

palavra = input('Insira uma palavra pra procurar pelas vogais: ')

#uniao
u = vogais.union(set(palavra))

u_list = sorted(list(u))

#diferenca
d = vogais.difference(set(palavra))

#intercecao
i = vogais.intersection(set(palavra))

encontrado = i

for vogal in encontrado:
    print(vogal)

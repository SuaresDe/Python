

data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
ano = input("Digite o ano atual: ")

digitos_data = [int(char) for char in data_nascimento if char.isdigit()][:4] 

digitos_ano = [int(char) for char in ano]

d1, d2, m1, m2 = digitos_data

n1, n2, n3, n4 = digitos_ano

soma_total = sum(digitos_data) + sum(digitos_ano)

print(" ")
print(f"Soma total : {soma_total}")
print(" ")
if soma_total == 0:
    print("O Louco")
elif soma_total == 1:
    print("O Mago")
elif soma_total == 2:
    print("A Sacerdotisa")
elif soma_total == 3:
    print("A Imperatriz")
elif soma_total == 4:
    print("O Imperador")
elif soma_total == 5:
    print("O Papa")
elif soma_total == 6:
    print("Os Enamorados")
elif soma_total == 7:
    print("O Carro")
elif soma_total == 8:
    print("A Força")
elif soma_total == 9:
    print("O Eremita")
elif soma_total == 10:
    print("A Roda da Fortuna")
elif soma_total == 11:
    print("A Justiça")
elif soma_total == 12:
    print("O Enforcado")
elif soma_total == 13:
    print("A Morte")
elif soma_total == 14:
    print("A Temperança")
elif soma_total == 15:
    print("O Diabo")
elif soma_total == 16:
    print("A Torre")
elif soma_total == 17:
    print("A Estrela")
elif soma_total == 18:
    print("A Lua")
elif soma_total == 19:
    print("O Sol")
elif soma_total == 20:
    print("O Julgamento")
elif soma_total == 21:
    print("O Mundo")

print(" ")
'''O Louco
0 O Louco

O Mago
I O Mago

A Sacerdotisa
II A Sacerdotisa

A Imperatriz
III A Imperatriz

O Imperador
IV O Imperador

O Papa
V O Papa

Os Enamorados
VI Os Enamorados

O Carro
VII O Carro

A Força
VIII A Força

O Eremita
IX O Eremita

A Roda da Fortuna
X A Roda da Fortuna

A Justiça
XI A Justiça

O Enforcado
XII O Enforcado

A Morte
XIII A Morte

A Temperança
XIV A Temperança

O Diabo
XV O Diabo

A Torre
XVI A Torre

A Estrela
XVII A Estrela

A Lua
XVIII A Lua

O Sol
XIX O Sol

O Julgamento
XX O Julgamento

O Mundo
XXI O Mundo'''
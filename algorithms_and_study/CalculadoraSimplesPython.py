#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    print(" ")
    print("Calculadora Simples!")
    print(" ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print(" ")
    opcao = int(input("Escolha uma opção de '1 a 5': "))
    
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao !=4 and opcao != 5:
        print("Opção inválida, tente novamente!")
        opcao = int(input("Escolha uma opção de '1 a 5': "))
        
    if opcao == 1:
        print(" ")
        print("Adição: ")
        print(" ")
        x = float(input())
        y = float(input(f"{x} + "))
        z = x + y
        print(f"{x} + {y} = {z}")
        
    if opcao == 2:
        print(" ")
        print("Subtração: ")
        print(" ")
        x = float(input())
        y = float(input(f"{x} - "))
        z = x - y
        print(f"{x} - {y} = {z}")
        
    if opcao == 3:
        print(" ")
        print("Multiplicação: ")
        print(" ")
        x = float(input())
        y = float(input(f"{x} * "))
        z = x * y
        print(f"{x} * {y} = {z}")
        
    if opcao == 4:
        print(" ")
        print("Divisão: ")
        print(" ")
        x = float(input())
        y = float(input(f"{x} / "))
        z = x / y
        print(f"{x} / {y} = {z}")
        
    if opcao == 5:
        print("Encerrando...")
        break


# In[ ]:





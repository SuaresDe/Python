#!/usr/bin/env python
# coding: utf-8

# In[ ]:


saldo = 0

while True:
    
    print(" ")
    print("Caixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")
    print(" ")
    opcao = int(input("Escolha uma opção '1-4': "))
    print(" ")

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao !=4:
        print("Opção inválida, tente novamente!")
        opcao = int(input("Escolha uma opção '1-4': "))
        
        print(" ")
    
    
    if opcao == 1:
        print(f"Saldo: {saldo}")
        print(" ")
    
    elif opcao == 2:
        deposito = float(input("Qual valor do deposito? "))
        saldo = saldo + deposito
        print("Deposito realizado com sucesso!")
        print(" ")
    
    elif opcao == 3:
        saque = float(input("Qual valor que deseja sacar? "))
        if saldo >= saque:
            saldo = saldo - saque
            print("Saque realizada com sucesso!")
            print(" ")
        else:
            print("Saldo insuficiente!")
            print(" ")
        
    elif opcao == 4:
        print(" ")
        print("Obrigado por usar o meu Caixa Eletrônico!")
        break
    
    


# In[ ]:





# In[ ]:





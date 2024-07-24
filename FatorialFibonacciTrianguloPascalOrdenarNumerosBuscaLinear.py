import math

def fatorial():
    n = int(input("Digite o número para fatorar: "))
    fatorial = math.factorial(n)
    print(f'O fatorial de {n} é: {fatorial}')

def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for i in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

def triangulo_pascal():
    quantidade_linhas = int(input("Digite a quantidade de linhas: "))
    print("\n")

    for i in range(quantidade_linhas):
        print(" " * (quantidade_linhas - i - 1), end=" ")

        for j in range(i + 1):
            coeficiente = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            print(coeficiente, end=" ")

        print()

def crescente():
    input_num = input("Digite vários números separados por vírgula: ")

    numeros = input_num.split(',')

    lista_num = [int(numero.strip()) for numero in numeros]

    lista_num.sort(key=int)
    print(f"Números em ordem crescente: {lista_num}")

def decrescente():
    input_num = input("Digite vários números separados por vírgula: ")

    numeros = input_num.split(',')

    lista_num = [int(numero.strip()) for numero in numeros]

    lista_num.sort(key=int, reverse=True) 
    print(f"Números em ordem decrescente: {lista_num}")

def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

    if resultado != -1:
        print(f"Elemento {elemento} encontrado no índice {resultado}.")
    else:
        print(f"Elemento {elemento} não encontrado na lista.")

def menu():
    while True:
        print("\nEscolha a operação matemática:")
        print("1 - Fatorial")
        print("2 - Sequência Fibonacci")
        print("3 - Triangulo de Pascal")
        print("4 - Ordenar numeros")
        print("5 - Busca linear")
        print("0 - Sair")
        escolha = input("Digite o número: ")

        if escolha == "0":
            break
        elif escolha == "1":
            fatorial()
        elif escolha == "2":
            num_termos = int(input("Digite o número de termos: "))
            fib_sequencia = fibonacci(num_termos)
            print(f"A sequência de Fibonacci com {num_termos} termos é {fib_sequencia}")
        elif escolha == "3":
            triangulo_pascal()
        elif escolha =="4":
            print("\nEm que ordem deseja ordenar?")
            print("1 - Crescente")
            print("2 - Decrescente")
            sub_escolha = int(input("Digite o número: "))
            if sub_escolha == 1:
                crescente()
            elif sub_escolha == 2:
                decrescente()
            else:
                menu()
        elif escolha == "5":
            lista = [10, 20, 30, 40, 50]  

            elemento = int(input("Digite o elemento a ser buscado de forma linear: "))

            resultado = busca_linear(lista, elemento)
            if resultado != -1:
                print(f"Elemento {elemento} encontrado no índice {resultado}.")
            else:
                print(f"Elemento {elemento} não encontrado na lista.")
        else:
            print("Opção inválida. Tente novamente.")

menu()

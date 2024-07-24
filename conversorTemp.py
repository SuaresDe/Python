def conversor_fagrenheit_para_celsius():
    tempF = float(input("Digite a temperatura em Fahrenheit: "))

    tempC = (tempF - 32) * 5/9

    print("")


def conversor_celsius_para_fahrenheit():
    tempC = float(input("Digite a temperatura em Celsius: "))

    tempF = (tempC * 9/5) + 32 

    print(f"Temperatura em Fahrenheit: {tempF}")

def menu():
    while True:
        print("\n")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("0 - Sair")

        escolha = int(input("Digite o numero: "))

        if escolha == 1:
            conversor_celsius_para_fahrenheit()
        elif escolha == 2:
            conversor_fagrenheit_para_celsius()
        elif escolha == 0:
            print("")
            break
        else:
            print("Opção inválida.")
            escolha = int(input("Digite novamente: "))

menu()
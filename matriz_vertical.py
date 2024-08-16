def criar_matriz_vertical(linhas, colunas):
    matriz = [[0] * colunas for _ in range(linhas)]
    contador = 1
    
    for j in range(colunas):
        for i in range(linhas):
            matriz[i][j] = contador
            contador += 1
            
    return matriz

def imprimir_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0]) if num_linhas > 0 else 0
    
    largura_maxima = len(str(num_linhas * num_colunas))
    
    for linha in matriz:
        print(" | ".join(f"{num:>{largura_maxima}}" for num in linha))

while True:
    try:
        num_linhas = int(input("Digite o número de linhas da matriz: "))
        num_colunas = int(input("Digite o número de colunas da matriz: "))
        if num_linhas <= 0 or num_colunas <= 0:
            print("O número de linhas e colunas deve ser maior que 0. Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

matriz = criar_matriz_vertical(num_linhas, num_colunas)
imprimir_matriz(matriz)

input_contagem = input("Digite algo: ")

numeros = 0
letras = 0
caracteres_especiais = 0
espacos_em_branco = 0

for caractere in input_contagem:
    if caractere.isdigit():  
        numeros += 1
    elif caractere.isalpha():  
        letras += 1
    elif caractere == " ":
        espacos_em_branco += 1
    else:
        caracteres_especiais += 1  

print(f"Números: {numeros}")
print(f"Letras: {letras}")
print(f"Caracteres especiais: {caracteres_especiais}")
print(f"Espaços em branco: {espacos_em_branco}")

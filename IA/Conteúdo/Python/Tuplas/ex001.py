# Criamos a tupla com os números por extenso
numeros = ("zero", "um", "dois", "três", "quatro", "cinco")

n = int(input("Digite um número entre 0 e 5: "))

# Verificamos se o número está no intervalo válido
if 0 <= n <= 5:
    # Usamos o próprio número digitado como índice da tupla!
    print(f"Você digitou o número {numeros[n]}.")
else:
    print("Número inválido! Tente novamente.")
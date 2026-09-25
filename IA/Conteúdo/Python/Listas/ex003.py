lista = []

for i in range(1, 6):
    n = int(input("Digite um número: "))
    lista.append(n)

print("Primeiro número:", lista[0])
print("Último número:", lista[-1])
print("Na posição par:", lista[::2])
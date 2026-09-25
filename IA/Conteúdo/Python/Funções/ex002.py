

def calcular_area(largura, comprimento):
    a = largura * comprimento
    return a

l = int(input("Digite a largura do terreno (em metros): "))


c = int(input("Digite o comprimento do terreno (em metros): "))

resposta = calcular_area(l, c)
print(f"Área do terreno: {resposta}")
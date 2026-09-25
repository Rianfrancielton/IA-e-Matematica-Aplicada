v = float(input("Digite a velocidade de um carro (Em km/h): "))

m = v - 80
vm = m * 7

if v > 80:
    print(f"Você foi multado! Valor: {vm}R$")
elif v <= 80:
    print("Você está dentro do limite.")
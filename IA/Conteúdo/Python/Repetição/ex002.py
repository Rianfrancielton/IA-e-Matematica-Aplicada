
while True:
    s = str(input("Digite o sexo de uma pessoa (M ou F): ")).strip().upper()
    if s != "M" and s != "F":
        print("Digite apenas M ou F!")
    else:
        print("sexo digitado com sucesso!")
        break
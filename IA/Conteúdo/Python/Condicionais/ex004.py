v_casa = float(input("Digite o valor da casa: "))
s_comprador = float(input("Digite o seu salário: "))
anos = float(input("Digite em quantos anos você vai pagar: "))

v_prestacao = v_casa/ (anos * 12)


if  v_prestacao <= (30/100) * s_comprador:
    print("Empréstimo Aprovado!")
else:
    print("Empréstimo negado!")

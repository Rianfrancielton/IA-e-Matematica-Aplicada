
n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))

opcao = 0
while opcao != 4:
    print()
    print("[1] Somar \n[2] Multiplicar \n[3] Novos números \n[4] Sair do programa")
    print()
    opcao = int(input("Escolha um serviço do menu: "))
    print()
    if opcao == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif opcao == 2:
        print(f"{n1} x {n2} = {n1*n2}")
    elif opcao == 3:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite mais um número: "))
        print()
    elif opcao == 4:
        print("Programa Fonalizado!")
        break

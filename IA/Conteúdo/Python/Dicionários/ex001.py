pessoa = {}

no = input("Digite seu nome: ")
pessoa["nome"] = no

na = int(input("Digite seu ano de nascimento: "))
pessoa["ano_nascimento"] = na

calculo = 2026 - pessoa["ano_nascimento"]
pessoa["idade"] = calculo

print(pessoa)
print(f"{pessoa['nome']} tem {pessoa['idade']} anos")
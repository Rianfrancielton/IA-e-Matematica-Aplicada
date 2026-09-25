

def votar(ano_nasc):
    idade = 2026 - ano_nasc

    if idade < 16:
        return "Voto Negado!"
    elif idade == 16 or idade == 17 or idade > 70:
        return "Voto opcional!"
    elif idade >= 18 and idade <= 70:
        return "Voto obrigatório!"
    
a = int(input("Digite seu ano de nascimento: "))

resultado = votar(a)
print(resultado)
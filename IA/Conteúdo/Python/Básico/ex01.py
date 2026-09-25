#expressões lógicas: tabela verdade;
#comandos condicionais;

#Operador lógivo OR: O operador 'or' retorna True se pelo menos uma das condições for verdadeira.

#Enunciado: Uma loja concede frete grátis se o cliente for Membro Prime (P) OU se o valor da compra for maior que R$ 200 (Q).

prime = True;
compra = 150;

if prime or compra > 200:
    print("Frete grátis liberado!")
else:
    print("Frete grátis não disponível.")


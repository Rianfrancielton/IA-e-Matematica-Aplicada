#Enunciado: Um usuário pode acessar o sistema se NÃO estiver com a conta bloqueada ($\neg P$) E possuir uma senha válida ($Q$).

c_ativa = False
s_valida = True

if not c_ativa and s_valida:
    print("Acesso Permitido!")
else:
    print("Acesso Negado!")


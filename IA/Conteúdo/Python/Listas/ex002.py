alunos = ["Ana", "Carlos", "Gabriel"]

aluno = input("Insira o nome de um aluno para remover da lista: ")

print("Antes: ", alunos)

if aluno in alunos:
    alunos.remove(aluno)
else:
    print("Aluno não encontrado na lista!")

print("Depois: ", alunos)
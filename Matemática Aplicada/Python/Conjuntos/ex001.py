#Exercício da aula 02

class conjunto: 
    def __init__(self, elementos):
        self.elementos = elementos
    #construtor

    def uniao(self, B):
        uniao = self.elementos + B.elementos
        return MeuConjunto(uniao)
    #Método União

A = conjunto([1,1,10,5,9])
B = conjunto([5,9,20,30])

C = A.uniao(B)
print(C.elementos)

class MeuConjunto:

    def __init__(self, elementos=None):
        self.elementos = []

        if elementos is not None:
            for elemento in elementos:
                if elemento not in self.elementos:
                    self.elementos.append(elemento)

    def uniao(self, *outros_conjuntos):
        todos_elementos = list(self.elementos)

        for conjunto in outros_conjuntos:
            todos_elementos.extend(conjunto.elementos)

        return MeuConjunto(todos_elementos)

    def intersecao(self, *outros_conjuntos):
        elementos_comuns = []

        for elemento in self.elementos:
            presente_em_todos = True
            for conjunto in outros_conjuntos:
                if elemento not in conjunto.elementos:
                    presente_em_todos = False
                    break
            if presente_em_todos:
                elementos_comuns.append(elemento)

        return MeuConjunto(elementos_comuns)

    def __repr__(self):
        return f"MeuConjunto({self.elementos})"

A = MeuConjunto([1, 2, 3])
B = MeuConjunto([3, 4, 5])
C = MeuConjunto([3, 5, 6])
D = MeuConjunto([3, 7, 8])

u = A.uniao(B, C, D)
print("União de A, B, C e D:", u)

i = A.intersecao(B, C, D)
print("Interseção entre A, B, C e D:", i)
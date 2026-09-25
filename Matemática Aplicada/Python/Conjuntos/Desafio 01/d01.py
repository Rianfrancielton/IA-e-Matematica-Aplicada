
class MeuConjunto:

    def __init__(self, elementos=None):
        self.elementos = []

        if elementos is not None:
            for elemento in elementos:
                if elemento not in self.elementos:
                    self.elementos.append(elemento)

    def uniao(self, outro_conjunto):
        todos_elementos = self.elementos + outro_conjunto.elementos
        return MeuConjunto(todos_elementos)

    def intersecao(self, outro_conjunto):
        elementos_comuns = []

        for elemento in self.elementos:
            if elemento in outro_conjunto.elementos:
                elementos_comuns.append(elemento)
        return MeuConjunto(elementos_comuns)

    def __repr__(self):
        return f"MeuConjunto({self.elementos})"

c1 = MeuConjunto([1,2,3,3])
c2 = MeuConjunto([3,4,5])

u = c1.uniao(c2)
i = c1.intersecao(c2)

print("Conjunto c1 (sem duplicatas):", c1)
print("União entre c1 e c2:", u)
print("Interseção entre c1 e c2:", i)

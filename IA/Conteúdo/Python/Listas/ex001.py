compras = []

while len(compras) != 4:
    i = input("Adicione um item a lista: ")
    compras.append(i)
    
print("Lista cheia!")
compras.sort()
print(compras)


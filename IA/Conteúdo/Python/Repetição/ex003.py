
s = 0
v = []

for i in range(1, 6):
    n = int(input("Digite um número: "))
    v.append(n)
    s = s+n
print(f"{s}")
m = max(v)
print(f"O maior número digitado foi: {m}")
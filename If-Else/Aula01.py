a = input("Digite um número ")
b = input("Digite outro número ")

print(f"O resultado {a} > {b} é {a>b}")
print(f"O resultado {a} < {b} é {a<b}")
print(f"O resultado {a} >= {b} é {a>=b}")
print(f"O resultado {a} <= {b} é {a<=b}\n")

print("Tabela or:")
print(f"O resultado de {a}>{b} or {a}<{b}, ou seja, {a>b} or {a<b} é {a>b or a<b}")
print(f"O resultado de {a}>={b} or {a}<={b}, ou seja, {a>=b} or {a<=b} é {a>=b or a<=b}")
print(f"O resultado de {a}!={b} or {a}=={b}, ou seja, {a!=b} or {a==b} é {a!=b or a==b}")
print(f"O resultado de {a}=={b} or {a}<{b}, ou seja, {a==b} or {a<b} é {a==b or a<b}")
print(f"O resultado de {a}>{b} or {a}!={b}, ou seja, {a>b} or {a!=b} é {a>b or a!=b}")
print(f"O resultado de {a}<={b} or {a}=={b}, ou seja, {a<=b} or {a==b} é {a<=b or a==b}")
print(f"O resultado de {a}>{b} or {a}>={b}, ou seja, {a>b} or {a>=b} é {a>b or a>=b}")
print(f"O resultado de {a}!={b} or {a}>{b}, ou seja, {a!=b} or {a>b} é {a!=b or a>b}\n")

print("Tabela and:")
print(f"O resultado de {a}>{b} and {a}<{b}, ou seja, {a>b} and {a<b} é {a>b and a<b}")
print(f"O resultado de {a}>={b} and {a}<={b}, ou seja, {a>=b} and {a<=b} é {a>=b and a<=b}")
print(f"O resultado de {a}!={b} and {a}=={b}, ou seja, {a!=b} and {a==b} é {a!=b and a==b}")
print(f"O resultado de {a}=={b} and {a}<{b}, ou seja, {a==b} and {a<b} é {a==b and a<b}")
print(f"O resultado de {a}>{b} and {a}!={b}, ou seja, {a>b} and {a!=b} é {a>b and a!=b}")
print(f"O resultado de {a}<={b} and {a}=={b}, ou seja, {a<=b} and {a==b} é {a<=b and a==b}")
print(f"O resultado de {a}>{b} and {a}>={b}, ou seja, {a>b} and {a>=b} é {a>b and a>=b}")
print(f"O resultado de {a}!={b} and {a}>{b}, ou seja, {a!=b} and {a>b} é {a!=b and a>b}\n")

idade = int(input("Digite sua idade "))
if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

time = input("Para que time você torce?\n-> ")
if time == "São Paulo":
    print("O maior do Brasil")
else:
    print("Chora mais")



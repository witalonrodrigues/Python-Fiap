#Exercicio 1
valor1 = int(input("Digite um número "))
valor2 = int(input("Digite outro número "))
if valor1>valor2:
    print(f"O maior valor é {valor1}")
else:
    print(f"O maior valor é o {valor2}")

#Exercicio 2
anoNascimento = int(input("Digite seu ano de nascimento "))
if anoNascimento <= 2008:
    print("Você pode votar este ano")
else:
    print("Você não pode votar este ano")

#Exercicio 3
senha = input("Digite a senha ")
if senha != "1234":
    print("ACESSO NEGADO")
else:
    print("ACESSO PERMITIDO")

#Exercicio 4
numMaca = int(input("Quantas maçãs você comprou?\n"))
if numMaca >= 12:
    print(f"o valor total da compra foi {numMaca * 0.25} reais")
else:
    print(f"o valor total da compra foi {numMaca * 0.30} reais")

#Exercicio 5
valor1 = int(input("Digite um número "))
valor2 = int(input("Digite outro número "))
valor3 = int(input("Digite outro número "))

valores = [valor1, valor2, valor3]
valores.sort()

print("Os valores em ordem crescente são", valores)

#Exercicio 6
input("Digite seu gênero ")
sexo1 = "Feminino"
sexo2 = "Masculino"

altura = float(input("Digite sua altura "))

if sexo1:
     print(f"Seu peso ideal é {62.1 * altura - 44.7}")
else:
    print(f"Seu peso ideal é {72.7 * altura - 58}")

#Exercicio 7 e 8
numLados = int(input("Digite quantos lados tem o polígono "))
if numLados == 3:
    medida = float(input("Digite a medida do lado em cm "))
    print(f"TRIÂNGULO. Medida = {medida * medida / 2}")
elif numLados == 4:
    medida = float(input("Digite a medida do lado em cm "))
    print(f" QUADRADO. Medida = {medida * medida}")
elif numLados < 3:
    print("Não é um Polígono")
elif numLados == 5:
    print("PENTÁGONO")
else:
    print("Polígono não identificado")

#Exercicio 9
valor1 = int(input("Digite um número "))
valor2 = int(input("Digite outro número "))
valor3 = int(input("Digite outro número "))

maior_valor = max(valor1, valor2, valor3)
print(f"O maior valor é {maior_valor}")

#ADICIONAL
letra = input("Digite uma letra ")
if letra in "aeiou":
    print("Sua letra é uma vogal ")
else:
    print("Sua letra é uma consoante")


#Exercício 10
lado1 = float(input("Digite a medida do primeiro lado do triângulo "))
lado2 = float(input("Digite a medida do segundo lado do triângulo "))
lado3 = float(input("digite a medida do terceiro lado do triângulo "))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")

#Exercicio 11
lado1 = float(input("Digite o primeiro ângulo do triângulo "))
lado2 = float(input("Digite o segundo ângulo do triângulo "))
lado3 = float(input("Digite o terceiro ângulo do triângulo "))

if lado1 == 90 or lado2 == 90 or lado3 == 90:
    print("Triângulo Retângulo")
elif lado1 > 90 or lado2 > 90 or lado3 > 90:
    print("Triângulo Obtusângulo")
else:
    print("Triângulo Acutângulo")


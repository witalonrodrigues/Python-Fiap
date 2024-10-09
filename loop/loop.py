#Exercicio 1
while True:
    nota = input('Digite uma nota entre 0 e 10 ')
    if nota.isnumeric():
        nota = float(nota)
        if nota <= 10 and nota >= 0:
            print('Nota válida')
            break
        print('Nota inválida')
    

#Exercicio 2
nome = input('Digite um nome com mais que 3 caracteres ')
while len(nome) <= 3:
    nome = input('Digite um nome com mais que 3 caracteres ')
while True:
    idade = input('Digite uma idade entre 0 e 150 ')
    if idade.isnumeric():
        idade = int(idade)
        if idade <= 150 and idade >= 0:
            break     
while True:
    salario = input('Digite um salário maior que 0 ')
    if salario.isnumeric():
        salario = float(salario)
        if salario > 0:
            break
sexo = input('Digite o seu sexo (masculino = m, feminino = f) ')
while sexo != 'm' and sexo != 'f':
    sexo = input('Digite o seu sexo (masculino = m, feminino = f) ')
estadoCivil = input('Digite seu estado civil (s, c, v, d) ')
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    estadoCivil = input('Digite seu estado civil (s, c, v, d) ')

#Exercicio 3
a = 80
b = 200
ano = 0

while a < b:
    a *= 1.03
    b *= 1.015
    ano += 1
print(f'A quantidades de anos é: {ano}')

#Exercicio 4
numeros = 0
soma = 0

while numeros < 5:
    numero = float(input(f'Digite o {numeros + 1}º número '))
    soma += numero
    numeros += 1
    media = soma / 5
print(f'A soma dos 5 números é: {soma}')
print(f'A média dos 5 números é: {media}')

#Exercicio 5
num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
menor += 1
while menor < maior:
    print(menor)
    menor += 1
        

#Exercicio 6
while True:
    usuario = input('Digite o nome do usuário ')
    senha = input('Digite a senha ')
    if usuario != senha:
        break
    else:
        print('Usuario e senha não podem ser iguais')

#Exercicio 7
num = int(input('Digite qual tabuada deseja ver '))
i = 0
while i < 10:
    i += 1
    print(f'{num} x {i} = {num * i}')


#Exercicio 8

i = int(input('Digite quantos números você deseja ver '))
contador = 0
a, b = 1, 1

while i > contador:
    print(a)
    a, b = b, a + b
    contador += 1

#Exericicio 9

i = 0
impares = 0
pares = 0

while i < 10:
    num = int(input('Digite um número '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    i += 1

print(f'pares: {pares} impares: {impares}')

#Exercicio 10
num = int(input('Digite um número '))
fatorial = 1
print(f'{num}! = ', end='')
while num > 0:
    fatorial *= num
    print(f'{num}', end='')
    if num > 1:
        print(f'.', end='')
    num -= 1
print(f'= {fatorial}', end='')
    

#Exercicio 11
num = int(input('Digite um número '))
if num < 2:
    print(f'{num} não é um número primo')
else:
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            print(f'{num} não é primo ')
            break
        divisor += 1
    else:
        print(f'{num} é primo')

#Exercicio 12
num = int(input('Digite quantas notas deseja ver '))
i = 0
soma = 0
while i < num:
    notas = int(input('Digite as notas '))
    i += 1
    soma += notas
    media = soma / num
print(f'A média das notas é {media}')

#Exercicio 13
salario_inicial = float(input('Digite o salário inicial do funcionário '))
aumento = 0.015
ano = 1996
ano_atual = 2024
novo_salario = salario_inicial

while ano_atual > ano:
    novo_salario += novo_salario * aumento
    aumento *= 2
    ano += 1
    print(f'O salário do ano de {ano} é {novo_salario}')

#Exercicio 14
a = 0
b = 0 
c = 0
d = 0
i = 0
num = int(input('Digite quantos números deseja ver '))
while i < num:
    i += 1
    x = int(input(f'Digite o {i}º número '))
    if x < 0:
        print('Número Inválido, programa encerrado')
    elif x > 0 and x <= 25:
        a += 1
    elif x > 25 and x <= 50:
        b += 1
    elif x > 50 and x <= 75:
        c += 1
    elif x > 75 and x <= 100:
        d += 1
print(f'A quantidade de número entre 0 e 25 é {a}\n A quantidade de números entre 26 e 50 é {b}\n A quantidade de números entre 51 e 75 é {c}\n A quantidade de números entre 76 e 100 é {d}')

#Exercicio 15
eleitores = 10
jose = 0
joao = 0
nulo = 0
branco = 0
i = 0
while i < eleitores:
    i += 1
    voto = int(input('Digite seu voto '))
    if voto == 1:
        joao += 1
    if voto == 2:
        joao += 1
    if voto == 5:
        nulo += 1
    if voto == 6:
        branco += 1
percentual_b = branco * 100 / eleitores
percentual_n = nulo * 100 / eleitores
print(f'O número de votos para José foi {jose}')
print(f'O número de votos para João foi {joao}')
print(f'O número de votos brancos foi {branco}')
print(f'O número de votos nulos foi {nulo}')
print(f'{percentual_b}% de votos brancos')
print(f'{percentual_n}% de votos nulos')
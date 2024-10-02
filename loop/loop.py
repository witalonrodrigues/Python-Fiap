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
    a *= a 1.03
    b *= 1.015
    ano += 1
print(f'A quantidades de anos é: {ano}')

#Exercicio 4
numeros = 0
soma = 0

while numeros < 5:
    numero = float(input(f'Digite o {numeros + 1}º número '))
    while not numero.isnumeric:
        numero = float(input(f'Digite o {numeros + 1}º número '))
    soma += numero
    numeros += 1
    media = soma / 5
print(f'A soma dos 5 números é: {soma}')
print(f'A média dos 5 números é: {media}')

#Exercicio 5
num1 = int(input('Digite o primeiro número '))
num2 = int(input('Digite o segundo número '))
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print('Os números são iguais')
        

#Exercicio 6
while True:
    usuario = input('Digite o nome do usuário ')
    senha = input('Digite a senha ')
    if usuario != senha:
        break
    else:
    print('Usuario e senha não podem ser iguais')

#Exercicio 7
i = int(input('Digite qual tabuada deseja ver '))
j = 1
num = 0
while i < 11:
    while j < 11:
        print(f'{i} * {j} = {i*j}')
        j += 1

#Exercicio 8
n = int(input('Quantos números da série de Fibonacci deseja ver? '))
a, b = 0, 1

for _ in range(2, n):
    a, b = b, a + b
    print(a)

#Exercicio 9
pares = 0
impares = 0
i = 0
while i < 10:
    num = int(input('Digite um número '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(f'Pares: {pares}\n Ímpares: {impares}')

#Exercicio 10
numero = int(input('Digite um número '))
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
    print(f'{numero}! = {fatorial}')

#Exercicio 11
i = 2
num = int(input('Digite um número '))
while True:
    i += 1
    if num % i == 0:
        print(f'{num} não é primo')
        break
    elif i == num-1:
        print(f'{num} é primo')
        break

#Exercicio 12
i = 0
num = int(input('Quantas notas deseja saber a média? '))
soma = 0
while i < num:
    nota = int(input('Digite as notas '))
    soma += nota
    i += 1
    media = soma / num
print(f'A média aritmética é: {media} ')

#Exercicio 13
ano = int(input('Digite após quantos anos você deseja ver o salário '))
salarioInicial = int(input('Digite o salário inicial '))
i = 0
taxa = 0.015
while i < ano:
    if ano == 1:
        salario = salarioInicial * (taxa+1)
        print(f'O salário será {salario}')
        i += 1
    else:
        taxa *= 2
        salario = salarioInicial * (taxa+1)
        i += 1
        print(f'O salário será {salario}')

#Exercicio 14
contagem1 = 0
contagem2 = 0
contagem3 = 0
contagem4 = 0
n = int(input('Quantos números você deseja verificar? '))
i = 0
num = int(input('Digite um número '))
while i < n :
    if num >= 0 and num <= 25:
        contagem1 += 1
    elif num >= 26 and num <= 50:
        contagem2 += 1
    elif num >= 51 and num <= 75:
        contagem3 += 1
    elif num >= 76 and num <= 100:
        contagem4 += 1
    print(f'entre 0 e 25:{contagem1}\n entre 26 e 50: {contagem2}\n entre 51 e 76: {contagem3}\n entre 76 e 100: {contagem4}')











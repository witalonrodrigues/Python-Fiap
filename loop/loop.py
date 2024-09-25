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
    soma += numero
    numeros += 1
    media = soma / 5
print(f'A soma dos 5 números é: {soma}')
print(f'A média dos 5 números é: {media}')

#Exercicio 5








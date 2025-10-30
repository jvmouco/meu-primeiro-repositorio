# 1. Identificação de Tipos:
# Crie variáveis que representem:
# sua idade
# sua altura
# seu nome
# se você é estudante
# Depois, use a função type() para mostrar o tipo de cada variável
idade = 18
Altura = 1.75
nome = "Vinicius"
eh_estudante = True
type(eh_estudante)
type(idade)
type(Altura)
type(nome)


# 2. Conversão de Tipos:
# O usuário digita a sua idade.
# Converta essa entrada para número inteiro.
# Some +5 anos e mostre o resultado.
idade = input("Digite sua idade: ")
idade = int(idade)
print("Sua idade atual é:", idade)
print("Sua idade daqui 5 anos é:", idade + 5)


# 3. Soma de Números Inteiros:
# Leia dois números inteiros e exiba a soma deles. 
# Entrada: Dois números inteiros. 
# Saída: A soma dos dois números. 
# Exemplo: Entrada: 3, 5 Saída: 8
num1=int(input("Digite o primeiro número"))
num2=int(input("Digite o segundo número"))
soma=num1 + num2
print("A soma dos números é:", soma)


# 4. Média de Três Números Inteiros Enunciado:
# Escreva um programa que leia três números inteiros e determine a média deles. 
# Entrada: Três números inteiros.
# Saída: Média dos três números. 
# Exemplo: 
# Entrada: 5, 1, 12 
# Saída: 6
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
media = (num1 + num2 + num3)/3
media = float(media)
print("A média é:", media)


# 5. Média Ponderada (Padrão Ibmec):
# Escreva um programa que receba as 3 notas das avaliações dos alunos e determine a média final através da ponderação padrão do Ibmec. 
# Entrada: Três números (notas). 
# Saída: Nota Final. 
# Exemplo: 
# Entrada: 5, 6.5, 10 
# Saída: 6
AP1 = input("Digite a primeira nota: ")
AP2 = input("Digite a segunda nota: ")
AC = input("Digite a terceira nota: ")
AP1 = float(AP1)
AP2 = float(AP2)
AC = float(AC)
media = (AP1 * 0.4 + AP2 * 0.4 + AC * 0.2)
media = float(media)
print("A média das notas é:", media)


# 6. Manipulação de Strings:
# Peça o nome completo do usuário.
# Mostre o nome em letras maiúsculas.
# Mostre apenas o primeiro nome.
# Mostre a quantidade de letras do nome (sem contar os espaços).
nome = input("Digite seu nome completo: ")
nome.upper()
print("seu nome em letra maíuscula é:", nome.upper())
primeiro_nome = nome.split()[0]
print("Seu primeiro nome é:", primeiro_nome)
quantidade_letras = len(nome)
print("quantidade:", quantidade_letras)

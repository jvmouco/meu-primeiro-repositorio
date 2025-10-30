# 1. Par ou ímpar
# Leia um número inteiro e identifique se é impar ou par:
numero = int(input("Digite um número: "))
if numero %2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 2. aprovado ou reprovado 
# Leia a nota final de um aluno e diga se ele está:
# Aprovado, se a nota for maior ou igual a 7.
# Reprovado, se a nota for menor que 7.
nota = float(input("Digite a sua nota:"))
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# 3. Cálculo de Desconto
# Leia o valor de uma compra.
# Se o valor for maior que 100, aplicar 10% de desconto.
# Caso contrário, não aplicar desconto.
# Mostrar o valor final.
valor = float(input("Digite o valor da compra"))
if valor > 100:
    desconto = valor * 0.1
    valor_final = valor - desconto
else:
    desconto = valor
print(f"total a pagar é: {valor_final:.2f}")

# 4. Conversão de Temperatura
# Leia a temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = (C x 9/5) + 32.
temperatura=float(input("digite a temperatura em C:"))
F = (temperatura * 9/5) + 32
print(f"A temperatura em F é: {F:.2f}")

# 5. Maior Número (Dois Valores)
# Leia dois números inteiros e informe:
# Qual deles é o maior.
# Ou se são iguais.
num1=int(input("Digite o primeiro numero:"))
num2=int(input("Digite o segundo numero:"))
if num1 > num2:
    print(f"O maior núemro é:", num1)
elif num2 > num1:
    print(f"O maior número é:", num2)
else:
    print("Os números são iguais")

# 6. Maior Número (Três Valores)
# Escreva um programa que leia três números inteiros e determine qual deles é o maior.
# Entrada: Três números inteiros.
# Saída: O maior número.
# Exemplo:
# Entrada: 7, 2, 9
# Saída: 9
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f"O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print(f"O maior número é:", num2)
elif num3 > num1 and num3 > num2:
    print(f"O maior número é:", num3)
else:
    print("Todos os números são iguais")

# 7. Calculadora Simples
# Crie uma calculadora simples que permita ao usuário realizar operações básicas: soma (+), subtração (-), multiplicação (*) e divisão (/).
# Entrada: Dois números e a operação desejada.
# Saída: O resultado da operação.
# Exemplo:
# Entrada: 8, 4, "/"
# Saída: 2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operacao desejada (+, -, *, /):")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero"
print("Resultado:", resultado)

# 8. Contagem de Números
# Leia uma sequência de números inteiros e conte quantos são positivos, negativos e zeros.
# Entrada: Lista de números inteiros (o usuário decide quantos números serão inseridos).
# Saída: Quantidade de números positivos, negativos e zeros.
# Exemplo:
# Entrada: [3, -1, 0, 7, -5]
# Saída: 2 positivos, 2 negativos, 1 zero
positivos = 0
negativos = 0
zeros = 0
quantidade = int(input("Quantos números você quer digitar? "))
for i in range(quantidade):
    numero = float(input("Digite os números:"))
    if numero > 0:
     positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1
print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Números zeros:", zeros)

# 9. Ano Bissexto
# Leia um número inteiro representando um ano e verifique se ele é bissexto ou não.
# Entrada: Um ano (número inteiro).
# Saída: "Bissexto" ou "Não é bissexto".
# Exemplo:
# Entrada: 2024
# Saída: Bissexto
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")

# 10. Intervalo de Idade
# Leia a idade de uma pessoa e informe se ela está na faixa etária permitida (18 a 65 anos).
# Se a idade estiver entre 18 e 65 (inclusive), mostrar: "Dentro da faixa permitida".
# Caso contrário, mostrar: "Fora da faixa permitida".
# (Use >= e <= com and).
idade=int(input("Digite sua idade"))
if idade >= 18 and idade <= 65:
    print("Dentro da faixa etária permitida")
else:
    print("Fora da faixa etrária permitida")

# 11. Acesso ao Sistema
# Leia o usuário e a senha digitados.
# Se usuário == "admin" e senha == "1234", mostrar: "Acesso permitido".
# Caso contrário, mostrar: "Acesso negado".
# (Use == e and).
Usuário=input("Digite o usuário")
Senha=input("Digite a senha:")
if Usuário == "admin" and Senha == "1234":
    print("Acesso permitido:")
else:
    print("Acesso negado")

# 12. Voto Obrigatório
# Leia a idade de uma pessoa.
# Se a idade for menor que 16, mostrar "Não vota".
# Se a idade for entre 18 e 70, mostrar "Voto obrigatório".
# Caso contrário, mostrar "Voto facultativo".
# (Use combinações com and e or).
idade=int(input("Digite sua idade"))
if idade < 16:
    print("Nao vota")
elif idade >= 16 and idade < 18 or idade >=70:
    print("Voto Facultativo")
elif idade >=18 or idade >= 70:
    print("Voto obrigatório")

# 13. Número Fora de Intervalo
# Leia um número inteiro e verifique:
# Se o número não está no intervalo de 10 a 50, mostrar "Fora do intervalo".
# Caso contrário, mostrar "Dentro do intervalo".
# (Use not com >= e <=).
numero=int(input("Digite o número"))
if numero >=10 and numero <=50:
    print("dentro do intervalo")
else:
    print("fora do intervalo")

# 14. Aluno Aprovado com Recuperação
# Leia a média final de um aluno.
# Se a média for >= 7, mostrar "Aprovado".
# Se a média for >= 5 e < 7, mostrar "Recuperação".
# Caso contrário, mostrar "Reprovado".
#(Use and, >=, <).
media = float(input("Digite a média final"))
if media >= 7:
    print("Arovado")
elif media >= 5 and media < 7:
    print("Recuperacao")
else:
    print("reprovado")




    




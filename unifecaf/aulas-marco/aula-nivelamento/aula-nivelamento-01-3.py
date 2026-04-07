# Crie um programa que solicite um número
# ao usuário e determine se ele é positivo
# negativo ou zero.

numero = int(input("Digite um número: "))

if numero > 0:
    print("É positivo!")
elif numero < 0: 
    print("É negativo!")
else: 
    print("É zero!")
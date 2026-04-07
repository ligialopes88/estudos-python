# calcule e apresente o valor do volume de 
# uma lata de óleo, utilizando a fórmula:
# volume = π * raio ** 2 altura
# considere o valor π de como 3.14159

raio = float(input ("Digite o raio da lata: "))
altura = float(input ("Digite a altura da lata: "))
PI = 3.14159

volume = PI * raio ** 2 * altura 

print(f"O volume da lata de óleo é: {volume}")
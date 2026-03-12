numero = input("Digite o numero: ")
base = int(input("Digite a base (8, 10 ou 16): "))

valor = int(numero, base)

print("Valor em decimal: ", valor)
print("Valor em hexadecimal: ", hex(valor))
print("Valor em octal: ", oct(valor))

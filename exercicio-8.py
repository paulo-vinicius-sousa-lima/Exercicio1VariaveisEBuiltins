#Aplicativo que criptografa:

inteiro = input("Digite um inteiro de 4 digitos para criptografar: ")

d1 = (int(inteiro[0]) + 7) % 10
d2 = (int(inteiro[1]) + 7) % 10
d3 = (int(inteiro[2]) + 7) % 10
d4 = (int(inteiro[3]) + 7) % 10

cripto = f"{d3}{d4}{d1}{d2}"

print(f"Numero criptografado: {cripto}")


#Aplicativo que descriptografa:

inteiroCripto = input("Digite um inteiro de 4 digitos para descriptografar: ")

d1 = int(inteiroCripto[2])
d2 = int(inteiroCripto[3])
d3 = int(inteiroCripto[0])
d4 = int(inteiroCripto[1])

d1 = (d1 + 3) % 10
d2 = (d2 + 3) % 10
d3 = (d3 + 3) % 10
d4 = (d4 + 3) % 10

descripto = f"{d1}{d2}{d3}{d4}"

print(f"Numero descriptografado: {descripto}")

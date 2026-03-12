texto = input("Digite o texto: ")
deslocamento = int(input("Deslocamento: "))

resultado = ""

for letra in texto:
    if 'A' <= letra <= 'Z':
        resultado += chr((ord(letra) - ord('A') + deslocamento) % 26 + ord('A'))

    elif 'a' <= letra <= 'z':
        resultado += chr((ord(letra) - ord('a') + deslocamento) % 26 + ord('a'))

    else:
        resultado += letra

print(f"{resultado}")

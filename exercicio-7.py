frase = input("Digite uma frase: ").lower()
qntVogais = 0

for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        qntVogais += 1

print(f"Quantidade de vogais: {qntVogais}")

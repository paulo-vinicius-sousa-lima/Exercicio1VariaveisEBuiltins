print("Escreva uma String no formato: 'YYYY-MM-DD HH:MM:SS - mensagem'")
string = input("Entrada: ")

data = string[0:10]
hora = string[11:19]
mensagem = string[22:]

print(f"DATA: {data}")
print(f"HORA: {hora}")
print(f"MENSAGEM: {mensagem}")

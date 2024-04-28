usuarios = list()
usuario = dict()
cont = 0
number = []

while True:
    usuario['user'] = str(input('Nome: '))
    usuario['senha'] = str(input('Senha: '))
    usuarios.append(usuario)
    
    print(usuario)

response = int(input('Digite um número'))

for x in range(response):
    response = int(input('Digite um número qualquer: '))
    response += 3
    number.append(response)
    cont += 1

print(number)
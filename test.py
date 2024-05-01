movieRoom = {
    'Sala A' : 25, 'occupation A' : 1,
    'Sala B' : 60, 'occupation B' : 1,
    'Sala C' : 40, 'occupation C' : 1,
    'Sala D' : 60, 'occupation D' : 1,
}

for sala in movieRoom:
    if 'Sala' in sala:
        imageSala = f'{sala}, Capacidade: {movieRoom[sala]}'
    else:
        if movieRoom[sala] != 1:
            imageSala += ', Sala Livre'
            print(imageSala)
        else:
            imageSala += ', Sala Ocupada'    
            print(imageSala)
print('\n')
print(movieRoom)
print('\n')  


# selectRoom = input('Qual sala o filme ocupará? [A/B/C/D] \nSala: ').upper()
# occupationRoom = 'occupation ' + selectRoom
# selectRoom = 'Sala ' + selectRoom
# for sala in movieRoom:
#     if selectRoom == sala:
#         if movieRoom[occupationRoom] == 0:
#             print('A sala não está ocupada e o filme foi cadastrado com sucesso')
#             movieRoom[occupationRoom] = 1
#         else:
#             print('A sala está ocupada')
            

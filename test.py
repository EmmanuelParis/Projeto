salaSelected = 'Sala A'
recognizedBuyChairs = True
movieRoom = {
    'Sala A' : 30, 'Occupation A' : 0,
    'Sala B' : 40, 'Occupation B' : 0,
    'Sala C' : 30, 'Occupation C' : 0,
    'Sala D' : 40, 'Occupation D' : 0,
}

chairsMovieRoom = {
    'Sala A' : [],
    'Sala B' : [],
    'Sala C' : [],
    'Sala D' : [],
}

for key in list(movieRoom.keys()):
        if 'Sala' in key:
            for numberChair in range(movieRoom[key]):
                chairStatus = dict()
                chairStatus['seatNumber'] = numberChair
                chairStatus['busy'] = False
                chairStatus['indexChair'] = numberChair + 1
                chairsMovieRoom[key].append(chairStatus)

while True:
    recognizedBuyChairs = True
    for key in list(chairsMovieRoom.keys()):
        if salaSelected == key:
            for controlChairs in chairsMovieRoom[key]:
                if controlChairs['busy'] != False:
                    controlChairs['seatNumber'] = 'XX'
                    
                    if (controlChairs['indexChair']) % 5 == 0:
                        print(f'[{controlChairs["seatNumber"]}]\n')
                    else:
                        print(f'[{controlChairs["seatNumber"]}]', end=' ')
                    
                else:    
                    if (controlChairs['indexChair']) % 5 == 0 and controlChairs['indexChair'] < 9:
                        print(f'[0{controlChairs["seatNumber"]+1}]\n')
                    elif (controlChairs['indexChair']) % 5 == 0:
                        print(f'[{controlChairs["seatNumber"]+1}]\n')
                    elif (controlChairs['indexChair']) < 10:
                        print(f'[0{controlChairs["seatNumber"]+1}]', end =' ')
                    else:
                        print(f'[{controlChairs["seatNumber"]+1}]', end =' ')
                        
        while recognizedBuyChairs:
            buyChair = int(input('\nDigite o número da cadeira que deseja comprar: '))
            print(buyChair)
            for keyRoom in list(chairsMovieRoom.keys()):
                if keyRoom == salaSelected:
                    if buyChair == 0 or buyChair > movieRoom[keyRoom]:
                        print('Cadeira invalida')
                    else:
                        for keysRoomChair in chairsMovieRoom[key]:
                            if keysRoomChair['indexChair'] == (buyChair):
                                if keysRoomChair['busy'] != True:
                                    print('Cadeira comprada com sucesso')
                                    keysRoomChair['busy'] = True
                                    recognizedBuyChairs = False
                                    break
                                else:
                                    print('Cadeira ocupada, não pode ser comprada')
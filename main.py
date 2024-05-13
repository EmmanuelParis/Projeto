usuarios = [{
    'user' : 'emmanuel',
    'password' : '123',
    'age' : 18,
    'email' : 'emmanuel@gmail.com',
    'id' : 0,
    'bank' : 0,
    'ticket' : list(),
    },
            {
    'user' : 'well',
    'password' : '12345',
    'age' : 18,
    'email' : 'wellington@gmail.com',
    'id' : 1,
    'bank' : 0,
    'ticket' : list(),
    }]

movies = [{
    'title' : 'Perdido em Código',
    'genre' : 'ação',
    'sinopse' :'''No filme "Perdido em Código", mergulhe em um universo onde a linha entre realidade e virtualidade se desfaz. 
A trama acompanha Wellington, um talentoso programador em busca de uma solução revolucionária para um problema que assola a humanidade. 
Porém, durante um teste crucial de seu programa, ele é subitamente transportado para dentro do código, 
encontrando-se perdido em um mundo digital labiríntico, onde cada linha de código é uma realidade distinta.''',
    'ageRating' : '14',
    'release' : '01/12/2020',
    'duration' : '150',
    'hours' : '2',
    'minutes' : '30',
    'price'  : '24.99',
    'room' : 'Sala D',
    'time' : '1200',
    'rating' : '99%',
    'comments' : list()
}]

controlMovieeRooms = {
    'Sala A' : {},
    'Sala B' : {},
    'Sala C' : {},
    'Sala D' : {},
}

movieRoom = {
    'Sala A' : 30, 'occupation A' : 0, 'bought A' : 0,
    'Sala B' : 40, 'occupation B' : 0, 'bought B' : 0,
    'Sala C' : 30, 'occupation C' : 0, 'bought C' : 0,
    'Sala D' : 40, 'occupation D' : 1, 'bought D' : 0,
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

recognizedBuyChairs = True
recognized = False
recognizedRoom = True
while True:
    
# MENU PRINCIPAL
    # PRINT PARA LIMPAR TERMINAL
    while True:
        print("\033[H\033[J", end="")
        print('\033[35m=' * 50 )
        print('CINE SERTÃO'.center(50))
        print('<--------------->'.center(50))
        print('MENU PRINCIPAL'.center(50))
        print('=' * 50 ,'\033[36m \n')

        print('\033[34m[1] - CATÁLOGO \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR\033[m\n')

        option = input('\033[32mOpção: \033[m')

        if (option.isdigit()):
            option = int(option)
            break
        else:
            print('Opção informada Invalida!')
            input()
    
# SISTEMA DE CATÁLOGO
    if (option == 1):
        print("\033[H\033[J", end="")
        print('\033[35m=' * 50 )
        print('CATÁLOGO DE FILMES'.center(50))
        print('=' * 50 ,'\033[36m \n')
        contMovies = 0
        print(f'\33[34m--- Filmes Disponíveis ---\33[m\n')
        for movie in movies:
            print(f'\33[34mFilme {contMovies+1}\33[m: \33[36m{movie['title']}\33[m')
            contMovies += 1
        movieCatalog = input('\n\33[34mQual filme deseja visualizar? \nFilme: \033[m')
        for movie in movies:
            if movie['title'] == movieCatalog:
                print('\033[36m=' * 50) 
                print(f'\33[36mTítulo do filme: \033[33m{movie['title']}\n\033[36mGênero do filme: \033[33m{movie['genre']}\n\033[36mSinopse do Filme: \033[33m{movie['sinopse']}\n\033[36mFaixa etária permitida: \033[33m{movie['ageRating']}\n\033[36mData de lançamento: \033[33m{movie['release']}\n\033[36mDuração: \033[33m{movie['hours']} Hora(s) e {movie['minutes']} Minuto(s)\n\033[36mPreço do ingresso: \033[33mR${movie['price']}\n\033[36mSala: \033[33m{movie['room']}\n\033[36mHorário de streaming: \033[33m{movie['time'][0:2] + ':' + movie['time'][2:]}\n\033[36mAprovação: \033[33m{movie['rating']}\33[m')
                print('\033[36m=' * 50)
                input('\033[mPressione qualquer tecla para continuar!')
    
# SISTEMA DE LOGIN
    if (option == 2):
        print("\033[H\033[J", end="")
        usercounter = 0
        print('\033[35m=' * 50 )
        print('LOGIN'.center(50))
        print('=' * 50 ,'\033[36m \n')
        print('')
        print('Digite sair em usuário para sair!')
        print('')
        while recognized != True:
            username = input('\033[34mDigite seu usuário: \033[m')
            if username.lower() == 'sair':
                break
            else:
                for pearson in usuarios:
                    if pearson['user'] == username:
                        password = input('\033[34mDigite sua senha: \033[m')
                        if pearson['password'] != password:
                            print('\033[31mUsuário ou Senha iválidos!\033[m')
                        else:
                            recognized = True
                            print('\033[32mVocê está logado!\033[m')
                    usercounter += 1
                if usercounter == len(usuarios) or pearson['user'] != username:
                    print('\033[31mUsuário não encontrado\033[m')
                
# SISTEMA DE CADASTRO
    elif (option == 3):
        print("\033[H\033[J", end="")
        print('\033[35m=' * 50 )
        print('CADASTRO'.center(50))
        print('=' * 50 ,'\033[36m \n')
        print('')
        print('Digite sair em usuário para sair!')
        print('')
        #CONDIÇÃO DE RESET PARA O CADASTRO
        dataCorrect = False
        thirtyDaysMonth = [4,6,9,11]
        recognizedRegister = True
        recognizedEmail = True
        exitCount = 0

        while recognizedRegister:
            contUser = 0

            registerUser = str(input('\033[34mDigite seu nome de usuário: \033[m'))
            if registerUser.lower() == 'sair':
                exitCount += 1
                break
            else:
                #removedor de espaços no inicio e no fim do nome
                registerUser = registerUser.strip()
                if (registerUser.isspace()) or (len(registerUser) <= 1):
                    print('Nome de usuario invalido')
                else:
                    if (len(usuarios) == 0):
                        break
                    elif (len(usuarios) != 0):
                        for user in usuarios:
                            if (registerUser == user['user']):
                                print('Nome de usuario já registrado!')
                                print('Insira um outro nome.')
                                contUser += 1
                                break
                        if (contUser == 0):    
                            recognizedRegister = False
                        else:
                            recognizedRegister = True
        if exitCount == 1:
            pass
        else:   
            while True:
                firstPassword = str(input('\033[34mDigite sua senha: \033[m'))
                if (len(firstPassword) < 6) or (' ' in firstPassword):
                    print('A senha precisa ter pelo menos 6 digitos, e sem espaços!')
                else:
                    break
            #CHECAGEM DE SENHA
            while True:
                secondPassword = str(input('\033[34mConfirme a senha: \033[m'))
                if(firstPassword == secondPassword):
                    break
                else:
                    print('\033[33mAs senhas não coincidem, tente novamente.\033[m')
            #CHECAGEM DA DATA DE NASCIMENTO
            while (dataCorrect != True):

                age = input('\033[34mDigite a sua idade: \033[m')

                if (len(age) < 1) or (' ' in age):
                    print('Data informada invalida, ou com espaços!')
                else:
                    if (age.isdigit()):
                        age = int(age)
                        if (age >= 6) and (age < 89):
                            dataCorrect = True
                        elif (age < 6):
                            print('\033O usuário é muito novo para possuir cadastro\033')
                        else:
                            print('\033Usuario muito velho para possui cadastro\033')
                    else:
                        print('Idade informada incorreta')


                    
            #CHECAGEM DO EMAIL
            while recognizedEmail:
                contUser = 0
                userEmail = str(input('\033[34mDigite seu E-mail: \033[m')).lower()
                if (len(userEmail) < 2) or (' ' in userEmail):
                    print('Email informado invalido, ou com espaços!')
                else:
                    if (len(usuarios) == 0):
                        break
                    elif (len(usuarios) != 0):
                        for user in usuarios:
                            if (userEmail == user['email']):
                                print('\033[31mE-mail já registrado!\033[m')
                                print('\033[31mInsira um outro e-mail.\033[m')
                                contUser += 1
                                break
                            else:
                                recognizedEmail = True
                        if (contUser == 0):
                            if(userEmail[-4:] == ".com" and (userEmail.count("@") == 1)):
                                break
                            else:
                                print('\033[31mEmail informado errado\033[m')
                                recognizedEmail = True
            #CONTROLE DE ADMIN
            while(True):
                id = 0
                checkAdmin = input('\033[32mInforme o tipo de cadastro: \n[1] Cliente \n[2] Admin \nOpção: \033[m')
                if (checkAdmin.isdigit()): 
                    checkAdmin = int(checkAdmin)
                    if(checkAdmin == 1):
                        break
                    elif(checkAdmin == 2):
                        while (True):
                            adminKey = input("\033[36mDigite a palavra-chave para se registrar como ADMIN: \033[m")
                            if(adminKey == "senhafoda123"):
                                id = 1
                                print('\033[36mCadastrado como ADMIN!\033[m')
                                break
                            else:
                                print('\033[31mPalavra-chave incorreta!\033[m')
                        break
                    else:
                        print('\033[31mInforme uma opção válida\033[m')
                else:
                    print('Opção informada invalida!')
                    
            usuario = dict()
            usuario['user'] = registerUser
            usuario['password'] = firstPassword
            usuario['age'] = age
            usuario['email'] = userEmail
            usuario['id'] = id
            usuario['bank'] = 0
            usuario['ticket'] = list()
            usuarios.append(usuario)
            
            print('\033[36mCadastro concluido com Sucesso!\033[m')
            input('Pressione qualquer tecla para continuar!')
            
    elif option == 0:
        print("\033[H\033[J", end="")
        print('\033[35mEncerrando o programa! Até a próxima!\033[m')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')        
# CRUD - CLIENTE
    if recognized:
        for pearson in usuarios:
            if pearson['user'] == username:
                if pearson['id'] == 0:
                    while True:
                        print("\033[H\033[J", end="")
                        print('\033[35m=' * 50 )
                        print('CINE SERTÃO'.center(50))
                        print('<--------------->'.center(50))
                        print('MENU CLIENTES'.center(50))
                        print('=' * 50 ,'\033[36m \n')
                        print(f'Cash: {round(pearson['bank'],2)}\n')
                        actionMenu = input('\033[34mO que deseja fazer? \n[1] - Depositar Dinheiro \n[2] - Comprar Ingresso \n[3] - Avaliar Filme \n[0] - Deslogar \n\nOpção: \033[m')

                        if (actionMenu.isdigit()):
                            actionMenu = int(actionMenu)
                            if actionMenu == 0:
                                logOff = input('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m')
                                if(logOff.isdigit()):
                                    logOff = int(logOff)
                                    if logOff == 1:
                                        recognized = False
                                        break
                                else:
                                    print('Opção invalida!')
                                    input()
                            # DEPOSITO DE DINHEIRO DO USUARIO
                            elif actionMenu == 1:
                                while True:
                                    print("\033[H\033[J", end="")
                                    print('\033[35m=' * 50 )
                                    print('DEPOSITAR DINHEIRO'.center(50))
                                    print('=' * 50 ,'\033[36m \n')
                                    deposit = input('\033[34mDigite o valor que deseja depositar: \033[m')
                                    if deposit.isdigit() or deposit.isdecimal():
                                        deposit = float(deposit)
                                        pearson['bank']+= deposit
                                        print('\033[36mDepósito realizado com sucesso!\033[m')
                                        break
                                    else:
                                        print('\033[31mValor informado invalido!\033[m')
                            # COMPRA DE INGRESSO E EXEBIÇÃO DAS CADEIRA
                            elif actionMenu == 2:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('COMPRAR INGRESSO'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                recognizedBought = True
                                while recognizedBought:
                                    showMatrix = True
                                    contMovies = 0
                                    print(f'\033[34m--- Filmes Catalogados ---\033[m')
                                    for movie in movies:
                                        print(f'\033[34mFilme {contMovies+1}\033[m: \033[36m{movie['title']}\033[m')
                                        print(f'\033[34mValor do Ingresso: \033[36mR${movie['price']}\033[m')
                                        print(f'\033[34mFaixa etária: \033[36m{movie['ageRating']} anos\033[m')
                                        print(f'\033[34mSala: \033[36m{movie['room']}\033[m')
                                        print(f'\033[34mHorário: \033[36m{movie['time'][0:2] + ':' + movie['time'][2:]}\033[m')
                                        print(f'\033[34m-------------------------\033[m')
                                        print('\n')
                                        contMovies += 1
                                    selectFilme = input('\033[34mInforme qual dos filmes deseja comprar o ingresso ou "sair" para voltar: \033[m').lower()
                                    
                                    if selectFilme == 'sair':
                                        recognizedBought = False
                                    else:
                                        print('\n')
                                        count = 1
                                        for movie in movies:
                                            #EXIBIÇÃO DAS CADEIRAS E ESCOLHA DO ASSENTO
                                            if movie['title'].lower() == selectFilme and pearson['bank'] >= float(movie['price']) and str(pearson['age']) >= movie['ageRating']:
                                                count = 1
                                                salaSelected = movie['room']
                                                while showMatrix:
                                                    recognizedBuyChairs = True
                                                    for key in list(movieRoom.keys()):
                                                        if salaSelected == key:
                                                            print(f'\033[36mCash: {round(pearson['bank'],2)}\n\033[m')
                                                            for controlChairs in chairsMovieRoom[key]:
                                                                if controlChairs['busy'] != False:
                                                                    controlChairs['seatNumber'] = '\033[31mXX\033[m'
                                                                    
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
                                                                controlMultipleChairs = dict()
                                                                buyChair = int(input('\033[34m\nDigite o número da cadeira que deseja comprar ou 0 para voltar: \033[m'))
                                                                if buyChair == 0:
                                                                    showMatrix = False
                                                                    recognizedBuyChairs = False
                                                                elif pearson['bank'] < float(movie['price']):
                                                                    print('\033[31mSaldo insuficiente!\033[m')
                                                                    input('\033[mPressione qualquer tecla para continuar!')
                                                                    showMatrix = False
                                                                    recognizedBuyChairs = False
                                                                else:
                                                                    for keyRoom in list(chairsMovieRoom.keys()):
                                                                        if keyRoom == salaSelected:
                                                                            if buyChair > movieRoom[keyRoom]:
                                                                                print('\n\033[31mCadeira inválida!\033[m')
                                                                            else:
                                                                                for keysRoomChair in chairsMovieRoom[key]:
                                                                                    if keysRoomChair['indexChair'] == (buyChair):
                                                                                        if keysRoomChair['busy'] != True:
                                                                                            print('\n\033[34mCadeira comprada com sucesso!\033[m')
                                                                                            controlBought = str(f'bought {salaSelected[-1]}')
                                                                                            movieRoom[controlBought] = movieRoom[controlBought] + 1
                                                                                            controlMultipleChairs['titleMovie'] = movie['title']
                                                                                            controlMultipleChairs['ticketNumber'] = buyChair
                                                                                            pearson['ticket'].append(controlMultipleChairs)
                                                                                            pearson['bank'] -= float(movie['price'])
                                                                                            keysRoomChair['busy'] = True
                                                                                            recognizedBuyChairs = False
                                                                                            break
                                                                                        else:
                                                                                            print('\n\033[31mCadeira ocupada, não pode ser comprada!\033[m')
                                            elif (count == len(movies) and movie['title'] != selectFilme) or pearson['bank'] < float(movie['price']):
                                                print('\033[31mFilme inválido ou Saldo insuficiente!\033[m')
                                                input('\033[mPressione qualquer tecla para continuar!')
                                                recognizedBought = False
                                            elif str(pearson['age']) < movie['ageRating']:
                                                print('\033[31mA faixa etária não lhe permite assistir!\033[m')
                                                input('Pressione qualquer tecla para continuar!')
                                                recognizedBought = False
                                            else:
                                                count += 1           
                            # AVALIAÇÃO DE FILMES
                            elif actionMenu == 3:
                                recognizedComment = True
                                watchedMovies = list()
                                while recognizedComment:
                                    print("\033[H\033[J", end="")
                                    print('\033[35m=' * 50 )
                                    print('AVALIAR FILME'.center(50))
                                    print('=' * 50 ,'\033[36m \n')
                                    titleValidation = True
                                    count = 1
                                    if pearson['ticket']:
                                        for objects in pearson['ticket']:
                                            title = objects['titleMovie']
                                            if title in watchedMovies:
                                                pass
                                            else:
                                                watchedMovies.append(title)
                                        for watched in watchedMovies:
                                            for movie in movies:
                                                if watched == movie['title']:
                                                    print(f'\033[34mTítulo: \033[36m{movie['title']}')
                                                    print(f'\033[34mSinopse: \033[36m{movie['sinopse']}')
                                                    print('')
                                        while titleValidation:
                                            selectCommentMovie = input('\033[34mDigite o título do filme o qual deseja comentar: \033[m')
                                            if selectCommentMovie in watchedMovies:
                                                for watch in watchedMovies:
                                                    if watch == selectCommentMovie:
                                                        comment = dict()
                                                        userComment = input('\033[34mDigite seu comentário: \033[m')
                                                        comment['user'] = pearson['user']
                                                        comment['movieComment'] = selectCommentMovie
                                                        comment['comment'] = userComment
                                                        for objMovies in movies:
                                                            if(objMovies['title'] == selectCommentMovie):
                                                                objMovies['comments'].append(comment)
                                                                break
                                                        recognizedComment = False
                                                        titleValidation = False
                                                        print('\033[33mComentário adicionado com sucesso!\033[m')
                                                        input('Pressione qualquer tecla para continuar!')
                                                        break
                                            else:
                                                print('\033[31mFilme informado invalido!\033[m')
                                                
                                    else:
                                        print('\033[31mVocê não assistiu nenhum filme para poder avaliar.\033[m')
                                        input('Pressione qualquer tecla para continuar!')
                                        break 
                        else:
                            print('\033[31mOpção inválida!\033[m')
                            input('Pressione qualquer tecla para continuar!')

# CRUD - ADMIN
                elif pearson['id'] == 1:
                    while True:
                        print("\033[H\033[J", end="")
                        print('\033[35m=' * 50 )
                        print('CINE SERTÃO'.center(50))
                        print('<--------------->'.center(50))
                        print('MENU ADMIN'.center(50))
                        print('=' * 50 ,'\033[36m')
                        print('\n')
                        actionMenu = input('\033[34mO que deseja fazer? \n[1] - Cadastrar Filme \n[2] - Buscar Filme \n[3] - Remover Filme \n[4] - Atualizar Filme \n[5] - Gestão dos filmes \n[6] - Feedbacks dos filmes \n[0] - Deslogar \n\nOpção: \033[m')
                        print('\n')
                        if (actionMenu.isdigit()):
                            actionMenu = int(actionMenu)
                            if actionMenu == 0:
                                logOff = input('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m')
                                if(logOff.isdigit()):
                                    logOff = int(logOff)
                                    if logOff == 1:
                                        recognized = False
                                        break
                                else:
                                    print('Opção invalida!')
                                    input()
                            # CADASTRAR FILME
                            elif actionMenu == 1:
                                # RESET DA DATA DE LANÇAMENTO
                                releaseCorrect = False
                                thirtyDaysMonth = [4,6,9,11]
                                # RESET DA ESCOLHA DA SALA
                                recognizedRoom = True
                                recognizedTitle = True
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('CADASTRAR FILME'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                # INICIO DO CADASTRO DO FILME
                                while recognizedTitle:
                                    countMovie = 0
                                    movieTitle = input('\033[34mDigite o título do filme: \033[m')

                                    if (len(movies) == 0):
                                        break
                                    elif (len(movies) != 0):
                                        for movie in movies:
                                            if (movieTitle == movie['title']):
                                                print('Título de filme já registrado!')
                                                print('Insira um outro título.')
                                                countMovie += 1
                                                break
                                        if (countMovie == 0):
                                            recognizedTitle = False
                                            break
                                        else:
                                            recognizedTitle = True
                                movieGenre = input('\033[34mDigite o gênero do filme: \033[m')
                                sinopseMovie = input('\033[34mDigite a sinopse do filme: \033[m')
                                ageRating = input('\033[34mDigite a classificação de idade: \033[m')
                                movieDuration = input('\033[34mDigite a duração do filme em minutos: \033[m')  
                                movieHour = int(movieDuration) // 60
                                movieMinutes = int(movieDuration) % 60
                                
                                while (releaseCorrect != True):
                                    releaseDate = input('\033[34mDigite a data de lançamento: \033[m')    
                                    #CONDIÇÃO DE FILTRAGEM SEM AS BARRAS
                                    if (len(releaseDate) == 8 and len(releaseDate) > 0):
                                        releaseDate = "/".join([releaseDate[:2], releaseDate[2:]])
                                        releaseDate = "/".join([releaseDate[:5], releaseDate[5:]])

                                        releaseYear = int(releaseDate[6:])
                                        releaseDay = int(releaseDate[0:2])
                                        releaseMonth = int(releaseDate[3:5])
                                        #CHECAGEM SE O ANO É VALIDO
                                        if((releaseYear < 1944) or (releaseYear > 2025)):
                                            if(releaseYear < 1944):
                                                print('\033[31mSeu filme é muito antigo para passar aqui!\033[m')
                                            else:
                                                print('\033[31mFilme vai demorar muito para lançar!\033[m')
                                        #CHECAGEM SE O MES É VALIDO
                                        elif((releaseMonth) <= 0 or (releaseMonth > 12)):
                                            print('\033[31mMês digitado inválido\033[m')
                                        #CHECAGEM SE O DIA É VALIDO
                                        elif((releaseDay > 0) and (releaseDay <= 31)):
                                            #CHECAGEM DE ANO BISSEXTO
                                            if (releaseDay == 29 and releaseMonth == 2):
                                                if (releaseYear % 4 == 0 and releaseYear % 100 != 0) or (releaseYear % 400 == 0):
                                                    releaseCorrect = True
                                                else:
                                                    print('\033[31mData informada inválida!\033[m')
                                            elif ((releaseMonth in thirtyDaysMonth) and releaseDay < 31):
                                                    releaseCorrect = True
                                            elif ((releaseMonth not in thirtyDaysMonth) and releaseDay <= 31):
                                                    if (releaseMonth == 2 and releaseDay > 28):
                                                        print('\033[31mData informada inválida!\033[m')
                                                    else:
                                                        releaseCorrect = True
                                            else:
                                                print('\033[31mData informada inválida!\033[m')
                                        else:
                                            print('\033[31mData informada inválida!\033[m') 
                                    #CONDIÇÃO DE FILTRAGEM COM OS BARRA    
                                    elif (len(releaseDate) == 10 and releaseDate[2] == '/' and releaseDate[5] == '/'):
                                        releaseYear = int(releaseDate[6:])
                                        releaseDay = int(releaseDate[0:2])
                                        releaseMonth = int(releaseDate[3:5])
                                        #CHECAGEM SE O ANO É VALIDO
                                        if((releaseYear < 1944) or (releaseYear > 2025)):
                                            if(releaseYear < 1944):
                                                print('\033[31mSeu filme é muito antigo para passar aqui!\033[m')
                                            else:
                                                print('\033[31mFilme vai demorar muito para lançar!\033[m')
                                        #CHECAGEM SE O MES É VALIDO
                                        elif((releaseMonth) <= 0 or (releaseMonth > 12)):
                                            print('\033[31mMês digitado inválido\033[m')
                                        #CHECAGEM SE O DIA É VALIDO
                                        elif((releaseDay > 0) and (releaseDay <= 31)):
                                            #CHECAGEM DE ANO BISSEXTO
                                            if (releaseDay == 29 and releaseMonth == 2):
                                                if (releaseYear % 4 == 0 and releaseYear % 100 != 0) or (releaseYear % 400 == 0):
                                                    releaseCorrect = True
                                                else:
                                                    print('\033[31mData informada inválida!\033[m')
                                            elif ((releaseMonth in thirtyDaysMonth) and releaseDay < 31):
                                                    releaseCorrect = True
                                            elif ((releaseMonth not in thirtyDaysMonth) and releaseDay <= 31):
                                                    if (releaseMonth == 2 and releaseDay > 28):
                                                        print('\033[31mData informada inválida!\033[m')
                                                    else:
                                                        releaseCorrect = True
                                            else:
                                                print('\033[31mData informada inválida!\033[m')
                                        else:
                                            print('\033[31mData informada inválida!\033[m')          
                                    else:
                                        print('\033[31mData informada inválida!\033[m')
                                
                                while True:
                                    ticketPrice = input('\033[34mDigite o valor do ingresso: \033[m')
                                    if ticketPrice.isdigit() or ticketPrice.isdecimal():
                                        # FILTRAGEM DOS DOIS NÚMEROS APÓS A VÍRGULA E TRANSFORMANDO A STRING EM FLOAT
                                        dotPosition = ticketPrice.find('.') 
                                        ticketPrice = (float(ticketPrice[:dotPosition+3]))
                                        break
                                    else:
                                        print('\033[31mDigite um número!\033[m')
                                        ticketPrice = input('\033[34mDigite o valor do ingresso: \033[m')
                                # ESCOLHA DE SALA E SUA CAPACIDADE
                                print('\n')
                                print('\033[35m=' * 50 )
                                print('SALAS'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                # EXIBIÇÃO DAS SALAS POR MEIO DE LOOP
                                for key in list(movieRoom.keys()):
                                    if 'Sala' in key:
                                        imageSala = f'\033[34m{key}, Capacidade: {movieRoom[key]},\033[m'
                                    elif 'occupation' in key:
                                        if movieRoom[key] != 1:
                                            imageSala += '\033[36m Sala: LIVRE!\033[m'
                                            print(imageSala)
                                        else:
                                            imageSala += '\033[31m Sala: OCUPADA!\033[m'    
                                            print(imageSala)
                                print('\n')
                                # LOOP DE SELEÇÃO DE SALAS
                                while recognizedRoom:
                                    selectRoom = input('\033[34mQual sala o filme ocupará? [A/B/C/D] \nSala: \033[m').upper()
                                    occupationRoom = 'occupation ' + selectRoom
                                    selectRoom = 'Sala ' + selectRoom
                                    for sala in movieRoom:
                                        if selectRoom == sala:
                                            if movieRoom[occupationRoom] == 0:
                                                movieRoom[occupationRoom] = 1
                                                recognizedRoom = False
                                            else:
                                                print('\033[31mA sala está ocupada\033[m')         
                                                
                                while True:
                                
                                    movieTime = input(f'\033[34mDigite o horário que o filme vai passar na {'a'} [HH:MM]: \033[m')
                                    if len(movieTime) == 5 and movieTime[2] == ':':
                                        movieTime = movieTime[:2] + movieTime[3:]
                                        if movieTime.isdigit() and (movieTime[:2] >= '00' and movieTime[:2] < '24') and (movieTime[2:] >= '00' and movieTime[2:] < '60'):
                                            break
                                        else:
                                            print('\033[31mHorário Inválido\033[m')
                                    else:
                                        print('\033[31mHorário Inválido\033[m')
                                
                                print('\33[36mFilme Cadastrado com Sucesso!\33[m')
                                input('Pressione qualquer tecla para continuar!')
                                
                                ratingTomato = movieDuration[0] + movieTime[1] + '%'
                                movie = dict()
                                movie['title'] = movieTitle
                                movie['genre'] = movieGenre
                                movie['sinopse'] = sinopseMovie
                                movie['ageRating'] = ageRating
                                movie['release'] = releaseDate
                                movie['duration'] = movieDuration
                                movie['hours'] = movieHour
                                movie['minutes'] = movieMinutes
                                movie['price'] = ticketPrice
                                movie['room'] = selectRoom
                                movie['time'] = movieTime
                                movie['rating'] = ratingTomato
                                movie['comments'] = list ()
                                
                                movies.append(movie)
                            # BUSCAR FILME
                            elif actionMenu == 2:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('BUSCAR FILME'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                searchMethod = input('\33[34mQual método deseja utilizar para buscar o filme? \n[1] - Título \n[2] - Gênero \nOpção: \33[m')
                                
                                if (searchMethod.isdigit()):
                                    searchMethod = int(searchMethod)
                                    if searchMethod == 1:
                                        searchMovieTitle = input('\33[34mQual o título do filme? \33[m')
                                        for movie in movies:
                                            if movie['title'] == searchMovieTitle:
                                                print('\033[36m=' * 50) 
                                                print(f'\33[36mTítulo do filme: {movie['title']}\nGênero do filme: {movie['genre']}\nSinopse do Filme: {movie['sinopse']}\nFaixa etária permitida: {movie['ageRating']}\nData de lançamento: {movie['release']}\nDuração: {movie['hours']} Hora(s) e {movie['minutes']} Minuto(s)\nPreço do ingresso: R${movie['price']}\nSala: {movie['room']}\nHorário de streaming: {movie['time']}\nAprovação: {movie['rating']}\33[m')
                                                print('\033[36m=' * 50)
                                                input('Pressione qualquer tecla para continuar!')
                                    elif searchMethod == 2:
                                        searchMovieGenre = input('\33[34mQual o gênero do filme? \33[m')
                                        for movie in movies:
                                            if movie['genre'] == searchMovieGenre:
                                                print('\033[36m=' * 50)
                                                print(f'\033[36mTítulo do filme: {movie['title']}\nGênero do filme: {movie['genre']}\nSinopse do Filme: {movie['sinopse']}\nFaixa etária permitida: {movie['ageRating']}\nData de lançamento: {movie['release']}\nDuração: {movie['hours']} Hora(s) e {movie['minutes']} Minuto(s)\nPreço do ingresso: R${movie['price']}\nSala: {movie['room']}\nHorário de streaming: {movie['time']}\nAprovação: {movie['rating']}\33[m')
                                                print('\033[36m=' * 50,'\033[36m \n')
                                                input('Pressione qualquer tecla para continuar!')
                                    else:
                                        print('\033[31mDigite uma opção válida!\033[m')
                                        input('Pressione qualquer tecla para continuar!')
                                else:
                                    print('\033[31mOpção invalida!\033[m')
                                    input()
                            # REMOVER FILME   
                            elif actionMenu == 3:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('REMOVER FILME'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                
                                contMovies = 0
                                print(f'\33[34m~~ Filmes Cadastrados ~~\33[m')
                                for movie in movies:
                                            print(f'\33[34mFilme {contMovies+1}\33[m: \33[36m{movie['title']}\33[m')
                                            contMovies += 1
                                delMovie = input('\33[34mDigite o título do filme deseja remover:  \33[m')
                                contIndexDel = 0
                                for movie in movies:
                                    if movie['title'] == delMovie:
                                        indexRoom = movie['room'][-1]
                                        occupationRoom = str(f'occupation {indexRoom}')
                                        movieRoom[occupationRoom] = 0
                                        del movies[contIndexDel]
                                        print('\33[36mFilme Removido!\33[m')
                                    contIndexDel += 1
                                input('Pressione qualquer tecla para continuar!')
                            # ATUALIZAR FILME
                            elif actionMenu == 4:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('ATUALIZAR FILME'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                
                                contMovies = 0
                                print(f'\33[34m~~ Filmes Cadastrados ~~\33[m')
                                for movie in movies:
                                            print(f'\33[34mFilme {contMovies+1}\33[m: \33[36m{movie['title']}\33[m')
                                            contMovies += 1
                                attMovie = input('\33[34mDigite o título do filme deseja atualizar:  \33[m')
                                contIndexAtt = 0
                                for movie in movies:
                                    if movie['title'] == attMovie:
                                        attType = int(input('\33[34mEscolha a informação que deseja atualizar: \n[1] - Título \n[2] - Gênero \n[3] - Sinopse \n[4] - Classificação de Idade \n[5] - Duração \n[6] - Data de Lançamento \n[7] - Sala \n[8] - Horário \n[9] - Avaliação \n[0] - Voltar \nOpção: \33[m'))
                                        if attType == 0:
                                            break
                                        elif attType == 1:
                                            print(f'\33[33mTítulo Atual: {movie['title']}\33[m')
                                            newTitle = input('\33[34mDigite o novo título: \33[m')
                                            movie['title'] = newTitle
                                        elif attType == 2:
                                            print(f'\33[33mGênero Atual: {movie['genre']}\33[m')
                                            newGenre = input('\33[34mDigite o novo gênero: \33[m')
                                            movie['genre'] = newGenre
                                        elif attType == 3:
                                            print(f'\33[33mSinopse Atual: {movie['sinopse']}\33[m')
                                            newSinopse = input('\33[34mDigite a nova sinopse: \33[m')
                                            movie['sinopse'] = newSinopse
                                        elif attType == 4:
                                            print(f'\33[33mClassificação de idade Atual: {movie['ageRating']}\33[m')
                                            newAgeRating = input('\33[34mDigite a nova classificação de idade: \33[m')
                                            movie['ageRating'] = newAgeRating
                                        elif attType == 5:
                                            print(f'\33[33mDuração Atual: {movie['duration']}\33[m')
                                            newDuration = input('\33[34mDigite a nova duração do filme: \33[m')
                                            newHour = int(newDuration) // 60
                                            newMinutes = int(newDuration) % 60
                                            movie['duration'] = newDuration
                                            movie['hours'] = newHour
                                            movie['minutes'] = newMinutes
                                        elif attType == 6:
                                            print(f'\33[33mData de Lançamento Atual: {movie['release']}\33[m')
                                            newDate = input('\33[34mDigite a nova data de lançamento: \33[m')
                                            movie['release'] = newDate
                                        elif attType == 7:
                                            print(f'\33[33mSala Atual: {movie['room']}\33[m')
                                            occupationRoom = 'occupation ' + movie['room'][-1].upper()
                                            # movieRoom[occupationRoom] = 0
                                            newRoom = input('\33[34mDigite a nova sala: \33[m').upper()
                                            newOccupationRoom = 'occupation ' + newRoom
                                            newRoom = 'Sala ' + newRoom
                                            for sala in movieRoom:
                                                if newRoom == sala:
                                                    if movieRoom[occupationRoom] == 1 and movieRoom[newOccupationRoom] == 1:
                                                        print('\033[31mA sala está ocupada, é impossível fazer a troca.\033[m')
                                                    elif movieRoom[occupationRoom] == 1 and movieRoom[newOccupationRoom] == 0:
                                                        movieRoom[occupationRoom] = 0
                                                        movieRoom[newOccupationRoom] = 1
                                                        movie['room'] = newRoom
                                                        print('\033[32mTroca das salas realizada com sucesso!\033[32m')
                                                    else:
                                                        print('\033[31mA sala está ocupada\033[m')
                                        elif attType == 8:
                                            print(f'\33[33mHorário de Streaming Atual: {movie['time']}\33[m')
                                            newTime = input('\33[34mDigite o novo horário de streaming: \33[m')
                                            movie['time'] = newTime
                                        elif attType == 9:
                                            print(f'\33[33mAvaliação Atual: {movie['rating']}\33[m')
                                            newRating = input('\33[34mDigite a nova avaliação: \33[m')
                                            movie['rating'] = newRating
                                        else:
                                            print('\33[31mDigite uma opção válida!\33[m')
                                    input('Pressione qualquer tecla para continuar!')
                            # GESTÃO E CONTROLE DE ASSENTOS
                            elif actionMenu == 5:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('GESTÃO DOS FILMES'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                
                                while True:
                                    actionMenu = input('\033[34mO que deseja fazer? \n[1] - Filmes mais Vendidos \n[2] - Controle de assentos livres \n[0] - Voltar \n\nOpção: \033[m')

                                    if (actionMenu.isdigit()):
                                        actionMenu = int(actionMenu)
                                        if (actionMenu == 0):
                                            break
                                        elif (actionMenu == 1):
                                            #FILMES MAIS VENDIDOS
                                            majorTitle = 'abc'
                                            majorSeller = movieRoom['bought A']
                                            majorRoom = 'Sala A'
                                            for key in list(movieRoom.keys()):
                                                if 'bought' in key:
                                                    if majorSeller < movieRoom[key]:
                                                        majorSeller = movieRoom[key]
                                                        majorRoom = key[-1]
                                                        majorRoom = str(f'Sala {majorRoom}')
                                            for movie in movies:
                                                if majorRoom == movie['room']:
                                                    majorTitle = movie['title']
                                            print(f'\033[34mO filme mais vendido foi o \033[33m{majorTitle} \033[34mcom \033[33m{majorSeller} \033[34mvendas!')
                                        elif (actionMenu == 2):
                                            #CONTROLE DE ASSENTOS
                                            for key in list(movieRoom.keys()):
                                                if 'Sala' in key:
                                                    imageSala = f'\033[34m{key}, Capacidade: {movieRoom[key]},\033[m'
                                                elif 'bought' in key:
                                                    indexSala = key[-1]
                                                    indexSala = str(f'Sala {indexSala}')
                                                    if (movieRoom[indexSala] - movieRoom[key]) == 0:
                                                        imageSala += str('\033[31m SALA LOTADA!\033[m')
                                                        print(imageSala)
                                                    else:
                                                        imageSala += str(f'\033[36m Cadeiras Livres: \033[33m{movieRoom[indexSala] - movieRoom[key]} \033[m')
                                                        print(imageSala)
                                            pass
                                        else:
                                            print('\033[31mOpção digitada invalida\033[m')
                                            input('Pressione qualquer tecla para continuar!')

                                    else:
                                        print('\033[31mOpção invalida!\033[m')
                                        input('Pressione qualquer tecla para continuar!')

                            #GESTOR DE FEEDBACKS DO CLIENTE
                            elif actionMenu == 6:
                                print("\033[H\033[J", end="")
                                print('\033[35m=' * 50 )
                                print('FEEDBACKS'.center(50))
                                print('=' * 50 ,'\033[36m \n')
                                recognizedFeedback = True
                                countEndMovies = 1
                                print('\033[33m--- Filmes Cadastrados ---')
                                for movie in movies:
                                    print(f'\n\033[36m{movie['title']}')
                                
                                while recognizedFeedback:
                                    feedbackTitle = input('\n\033[34mDigite o título do filme que deseja ver os feedbacks: \033[m')
                                    for movieList in movies:
                                                if feedbackTitle == movieList['title']:
                                                    if (len(movieList['comments']) == 0):
                                                        print('\033[31mEsse filme não possui nenhum comentário\033[m')
                                                        input('Pressione qualquer tecla para continuar!')
                                                        recognizedFeedback = False
                                                        break
                                                    else:
                                                        for dictComments in movieList['comments']:
                                                            if (feedbackTitle == dictComments['movieComment']):
                                                                print('\033[35m=' * 50 )
                                                                print(f'\033[34mUsuário: \033[36m{dictComments['user']}')
                                                                print(f'\033[34mComentário: \033[36m{dictComments['comment']}')
                                                                print('\033[35m=' * 50 )
                                                                recognizedFeedback =  False
                                                        input('\033[mPressione qualquer tecla para continuar!')
                                                elif (countEndMovies > len(movies)):
                                                    print('\033[31mFilme não encontrado!\033[m')
                                                    input('Pressione qualquer tecla para continuar!')
                                                    break
                                                countEndMovies += 1
                                        

                        else:
                            print('\033[31mOpção informada invalida!\033[m')
                            input('Pressione qualquer tecla para continuar!')
    else:
        pass
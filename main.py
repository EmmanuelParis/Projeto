usuarios = [{
    'user' : 'emmanuel',
    'password' : '123',
    'age' : 18,
    'email' : 'emmanuel@gmail.com',
    'id' : 1
    }]

usuario = dict()

movies = list()
movie = dict()

movieRoom = {
    'Sala A' : 40, 'occupation A' : 0,
    'Sala B' : 60, 'occupation B' : 0,
    'Sala C' : 40, 'occupation C' : 0,
    'Sala D' : 60, 'occupation D' : 0,
}


recognized = False
recognizedRoom = True
while True:
    
# MENU PRINCIPAL
    print('\033[35m=' * 50 )
    print('CINE SERTÃO'.center(50))
    print('<--------------->'.center(50))
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50 ,'\033[36m \n')

    print('\033[34m[1] - CATÁLOGO \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR\033[m\n')

    option = int(input('\033[32mOpção: \033[m'))
    
# SISTEMA DE LOGIN
    if (option == 2):
        usercounter = 0
        print('\033[35m=' * 50 )
        print('LOGIN'.center(50))
        print('=' * 50 ,'\033[36m \n')
        while recognized != True:
            username = input('\033[34mDigite seu usuário: \033[m')
            for pearson in usuarios:
                if pearson['user'] == username:
                    password = input('\033[34mDigite sua senha: \033[m')
                    if pearson['password'] != password:
                        print('\033[31mUsuário ou Senha iválidos!\033[m')
                    else:
                        recognized = True
                        print('\033[32mVocê está logado!\033[m')
                usercounter += 1
            if usercounter == len(usuarios) and pearson['user'] != username:
                print('\033[31mUsuário não encontrado\033[m')

# SISTEMA DE CADASTRO
    elif (option == 3):
        print('\033[35m=' * 50 )
        print('CADASTRO'.center(50))
        print('=' * 50 ,'\033[36m \n')
        #CONDIÇÃO DE RESET PARA O CADASTRO
        dataCorrect = False
        thirtyDaysMonth = [4,6,9,11]
        recognizedRegister = True

        while recognizedRegister:
            contUser = 0
            registerUser = str(input('\033[34mDigite seu nome de usuário: \033[m'))

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

                   

        firstPassword = str(input('\033[34mDigite sua senha: \033[m'))
        #CHECAGEM DE SENHA
        while True:
            secondPassword = str(input('\033[34mConfirme a senha: \033[m'))
            if(firstPassword == secondPassword):
                break
            else:
                print('\033[33mAs senhas não coincidem, tente novamente.\033[m')
        #CHECAGEM DA DATA DE NASCIMENTO
        while (dataCorrect != True):

            birthdate = str(input('\033[34mDigite a data de nascimento [dd/mm/aaaa]: \033[m'))
            #CONDIÇÃO DE FILTRAGEM SEM AS BARRAS
            if (len(birthdate) == 8 and len(birthdate) > 0):
                birthdate = "/".join([birthdate[:2], birthdate[2:]])
                birthdate = "/".join([birthdate[:5], birthdate[5:]])

                birthdateYear = int(birthdate[6:])
                birthdateDay = int(birthdate[0:2])
                birthdateMonth = int(birthdate[3:5])
                #CHECAGEM SE O ANO É VALIDO
                if((birthdateYear < 1944) or (birthdateYear> 2024)):
                    print('\033[33mTem certeza que você está vivo?\033[m')
                #CHECAGEM SE O MES É VALIDO
                elif((birthdateMonth) <= 0 or (birthdateMonth > 12)):
                    print('\033[31mMês digitado inválido\033[m')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('\033[31mData informada inválida!\033[m')
                    elif ((birthdateMonth in thirtyDaysMonth) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in thirtyDaysMonth) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('\033[31mData informada inválida!\033[m')
                            else:
                                dataCorrect = True
                    else:
                        print('\033[31mData informada inválida!\033[m')
                else:
                    print('\033[31mData informada inválida!\033[m') 
            #CONDIÇÃO DE FILTRAGEM COM AS BARRAS    
            elif (len(birthdate) == 10 and birthdate[2] == '/' and birthdate[5] == '/'):
                birthdateYear = int(birthdate[6:])
                birthdateDay = int(birthdate[0:2])
                birthdateMonth = int(birthdate[3:5])
                #CHECAGEM SE O ANO É VALIDO
                if((birthdateYear < 1944) or (birthdateYear> 2024)):
                    print('\033[34mTem certeza que você está vivo?\033[m')
                #CHECAGEM SE O MES É VALIDO
                elif((birthdateMonth) <= 0 or (birthdateMonth > 12)):
                    print('\033[31mMês digitado inválido\033[m')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('\033[31mData informada inválida!\033[m')
                    elif ((birthdateMonth in thirtyDaysMonth) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in thirtyDaysMonth) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('\033[31mData informada inválida!\033[m')
                            else:
                                dataCorrect = True
                    else:
                        print('\033[31mData informada inválida!\033[m')
                else:
                    print('\033[31mData informada inválida!\033[m')          
            else:
                print('\033[31mData informada inválida!\033[m')
                
        #CHECAGEM DO EMAIL
        while (True):
            userEmail = input('\033[34mInforme seu email: \033[m').lower()
            if(userEmail[-4:] == ".com" and (userEmail.count("@") == 1)):
                break
            else:
                print('\033[31mEmail informado errado\033[m')
        #CONTROLE DE ADMIN
        while(True):
            id = 0
            checkAdmin = int(input('\033[32mInforme o tipo de cadastro: \n[1] Cliente \n[2] Admin \nOpção: \033[m'))
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
                
        age = 2024 - birthdateYear
        usuario['user'] = registerUser
        usuario['password'] = firstPassword
        usuario['age'] = age
        usuario['email'] = userEmail
        usuario['id'] = id
        usuarios.append(usuario.copy())
        
        print('\033[36mCadastro concluido com Sucesso!\033[m')
    elif option == 0:
        print('\033[35mEncerrando o programa! Até a próxima!\033[m')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')        
# CRUD - CLIENTE
    if recognized:
        for pearson in usuarios:
            if pearson['user'] == username:
                if pearson['id'] == 0:
                    print('\033[35m=' * 50 )
                    print('CINE SERTÃO'.center(50))
                    print('<--------------->'.center(50))
                    print('MENU CLIENTES'.center(50))
                    print('=' * 50 ,'\033[36m \n')
                    while True:
                        actionMenu = int(input('\033[34mO que deseja fazer? \n[1] - Depositar Dinheiro \n[2] - Comprar Ingresso \n[3] - Avaliar Filme \n[0] - Deslogar \n\nOpção: \033[m'))

                        if actionMenu == 0:
                            logOff = int(input('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m'))
                            if logOff == 1:
                                recognized = False
                                break
                    
# CRUD - ADMIN
                elif pearson['id'] == 1:
                    while True:
                        print('\033[35m=' * 50 )
                        print('CINE SERTÃO'.center(50))
                        print('<--------------->'.center(50))
                        print('MENU ADMIN'.center(50))
                        print('=' * 50 ,'\033[36m')
                        print('\n')
                        actionMenu = int(input('\033[34mO que deseja fazer? \n[1] - Cadastrar Filme \n[2] - Buscar Filme \n[3] - Remover Filme \n[4] - Atualizar Filme \n[5] - Controle e Feedback \n[0] - Deslogar \n\nOpção: \033[m'))
                        print('\n')
                        
                        if actionMenu == 0:
                            logOff = int(input('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m'))
                            if logOff == 1:
                                recognized = False
                                break
                            
                        elif actionMenu == 1:
                            # RESET DA DATA DE LANÇAMENTO
                            releaseCorrect = False
                            thirtyDaysMonth = [4,6,9,11]
                            # RESET DA ESCOLHA DA SALA
                            recognizedRoom = True
                            
                            print('\033[35m=' * 50 )
                            print('CADASTRAR FILME'.center(50))
                            print('=' * 50 ,'\033[36m \n')
                            # INICIO DO CADASTRO DO FILME
                            movieTitle = input('\033[34mDigite o título do filme: \033[m')
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
                                    if((releaseYear < 1944) or (releaseYear> 2024)):
                                        print('\033[31mData informada inválida!\033[m')
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
                                    if((releaseYear < 1944) or (releaseYear> 2024)):
                                        print('\033[31mData informada inválida!\033[m')
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
                            
                            ticketPrice = input('\033[34mDigite o valor do ingresso: \033[m')
                            # FILTRAGEM DOS DOIS NÚMEROS APÓS A VÍRGULA E TRANSFORMANDO A STRING EM FLOAT
                            dotPosition = ticketPrice.find('.') 
                            ticketPrice = (float(ticketPrice[:dotPosition+3]))
                            # ESCOLHA DE SALA E SUA CAPACIDADE
                            print('\n')
                            print('\033[35m=' * 50 )
                            print('SALAS'.center(50))
                            print('=' * 50 ,'\033[36m \n')
                            # EXIBIÇÃO DAS SALAS POR MEIO DE LOOP
                            for sala in movieRoom:
                                if 'Sala' in sala:
                                    imageSala = f'\033[34m{sala}, Capacidade: {movieRoom[sala]},\033[m'
                                else:
                                    if movieRoom[sala] != 1:
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

                            ratingTomato = movieDuration[0] + movieTime[1] + '%'
        
                            movie['title'] = movieTitle
                            movie['genre'] = movieGenre
                            movie['sinopse'] = sinopseMovie
                            movie['ageRating'] = ageRating
                            movie['hours'] = movieHour
                            movie['minutes'] = movieMinutes
                            movie['price'] = ticketPrice
                            movie['room'] = selectRoom
                            movie['time'] = movieTime
                            movie['rating'] = ratingTomato
                            movies.append(movie.copy())
                            
                        elif actionMenu == 2:
                            print('\033[35m=' * 50 )
                            print('BUSCAR FILME'.center(50))
                            print('=' * 50 ,'\033[36m \n')
                            searchMethod = int(input('\33[34mQual método deseja utilizar para buscar o filme? \n[1] - Título \n[2] - Gênero \nOpção: \33[m'))
                            if searchMethod == 1:
                                searchMovieTitle = input('\33[34mQual o título do filme? \33[m')
                                for movie in movies:
                                    if movie['title'] == searchMovieTitle:
                                        print(f'\33[36mTítulo do filme: {movie['title']}\nGênero do filme: {movie['genre']}\nSinopse do Filme: {movie['sinopse']}\nFaixa etária permitida: {movie['ageRating']}\nDuração: {movie['hours']} Horas e {movie['minutes']} Minutos\nPreço do ingresso: R${movie['price']}\nSala: {movie['room']}\nHorário de streaming: {movie['time']}\nAvaliação: {movie['rating']}\33[m')
                            elif searchMethod == 2:
                                searchMovieGenre = input('\33[34mQual o gênero do filme? \33[m')
                                for movie in movies:
                                    if movie['genre'] == searchMovieGenre:
                                        print(f'\33[36mTítulo do filme: {movie['title']}\nGênero do filme: {movie['genre']}\nSinopse do Filme: {movie['sinopse']}\nFaixa etária permitida: {movie['ageRating']}\nDuração: {movie['hours']} Horas e {movie['minutes']} Minutos\nPreço do ingresso: R${movie['price']}\nSala: {movie['room']}\nHorário de streaming: {movie['time']}\nAvaliação: {movie['rating']}\33[m')
                            else:
                                print('\33[31mDigite uma opção válida!\33[m')
                                
                        elif actionMenu == 3:
                            print('\033[35m=' * 50 )
                            print('REMOVER FILME'.center(50))
                            print('=' * 50 ,'\033[36m \n')
                            
                            contMovies = 0
                            for movie in movies:
                                        print(f'\33[34mFilme {contMovies+1}\33[m: \33[36m{movie['title']}\33[m')
                                        contMovies += 1
                            delMovie = input('\33[34mDigite o título do filme deseja remover:  \33[m')
                            contIndexDel = 0
                            for movie in movies:
                                if movie['title'] == delMovie:
                                    movieRoom[occupationRoom] = 0
                                    del movies[contIndexDel]
                                    print('\33[36mFilme Removido!\33[m')
                                contIndexDel += 1
                        
                        elif actionMenu == 4:
                            print('\033[35m=' * 50 )
                            print('ATUALIZAR FILME'.center(50))
                            print('=' * 50 ,'\033[36m \n')
                            
                            contMovies = 0
                            for movie in movies:
                                        print(f'\33[34mFilme {contMovies+1}\33[m: \33[36m{movie['title']}\33[m')
                                        contMovies += 1
                            attMovie = input('\33[34mDigite o título do filme deseja atualizar:  \33[m')
                            pass
    else:
        pass
usuarios = list()
usuario = dict()
recognized = False
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

        while recognized != True:
            print('\033[35m=' * 50 )
            print('LOGIN'.center(50))
            print('=' * 50 ,'\033[36m \n')
            username = input('\033[34mDigite seu usuário: \033[m')
            for pearson in usuarios:
                if pearson['user'] == username:
                    password = input('\033[34mDigite sua senha: \033[m')
                    if pearson['password'] != password:
                        print('\033[31mUsuário ou Senha iválidos!\033[m')
                    else:
                        recognized = True
                        print('\033[32mVocê está logado!\033[m')
            
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
            elif (len(usuario) != 0):
                for user in usuarios:
                    print('='*12)
                    print(user['user'])
                    if (registerUser in user['user']):
                        print('Nome de usuario já registrado!')
                        print('Ensira um outro nome.')
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
            #CONDIÇÃO DE FILTRAGEM SEM OS PARENTESES
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
            #CONDIÇÃO DE FILTRAGEM COM OS PARENTESES    
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
            userEmail = input('\033[34mInforme seu email: \033[m')
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
    if recognized == True:
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
                    print('\033[35m=' * 50 )
                    print('CINE SERTÃO'.center(50))
                    print('<--------------->'.center(50))
                    print('MENU ADMIN \n'.center(50))
                    print('=' * 50 ,'\033[36m')
                    while True:
                        actionMenu = int(input('\033[34mO que deseja fazer? \n[1] - Cadastrar Filme \n[2] - Buscar Filme \n[3] - Remover Filme \n[4] - Atualizar Filme \n[5] - Controle e Feedback \n[0] - Deslogar \n\nOpção: \033[m'))

                        if actionMenu == 0:
                            logOff = int(input('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m'))
                            if logOff == 1:
                                recognized = False
                                break
    else:
        pass
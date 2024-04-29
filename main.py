thirtyDaysMonth = [4,6,9,11]
usuarios = list()
usuario = dict()

while True:
    
    print('=' * 50 )
    print('CINE SERTÃO'.center(50))
    print('-'.center(50))
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50)

    print('[1] - CATÁLOGO \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR')

    option = int(input('\033[32mOpção: \033[m'))
    
    if (option == 2):
        recognized = False
        while recognized != True:
            username = input('Digite seu usuário: ')
            for i in usuarios:
                if i['user'] == username:
                    password = input('Digite sua senha: ')
                    if i['password'] != password:
                        print('A senha não remete ao usuário')
                    else:
                        recognized = True
                        print('\033[32mVocê está logado!\033[m')
            
    if (option == 3):
        #CONDIÇÃO DE RESET PARA O CADASTRO DO NASCIMENTO
        dataCorrect = False

        registerUser = str(input('Digite seu nome de usuário: '))
        firstPassword = str(input('Digite sua senha: '))
        #CHECAGEM DE SENHA
        while True:
            secondPassword = str(input('Confirme a senha: '))
            if(firstPassword == secondPassword):
                break
            else:
                print('As senhas não são iguais, tente novamente.')
        #CHECAGEM DA DATA DE NASCIMENTO
        while (dataCorrect != True):

            birthdate = str(input('Digite a data de nascimento [dd/mm/aaaa]: '))
            #CONDIÇÃO DE FILTRAGEM SEM OS PARENTESES
            if (len(birthdate) == 8 and len(birthdate) > 0):
                birthdate = "/".join([birthdate[:2], birthdate[2:]])
                birthdate = "/".join([birthdate[:5], birthdate[5:]])

                birthdateYear = int(birthdate[6:])
                birthdateDay = int(birthdate[0:2])
                birthdateMonth = int(birthdate[3:5])
                #CHECAGEM SE O ANO É VALIDO
                if((birthdateYear < 1944) or (birthdateYear> 2024)):
                    print('Tem certeza que você está vivo?')
                #CHECAGEM SE O MES É VALIDO
                elif((birthdateMonth) <= 0 or (birthdateMonth > 12)):
                    print('Mês digitado inválido!')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('Data informada inválida!')
                    elif ((birthdateMonth in thirtyDaysMonth) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in thirtyDaysMonth) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('Data informada invalida')
                            else:
                                dataCorrect = True
                    else:
                        print('Data informada invalida')
                else:
                    print('Data informada invalida') 
            #CONDIÇÃO DE FILTRAGEM COM OS PARENTESES    
            elif (len(birthdate) == 10 and birthdate[2] == '/' and birthdate[5] == '/'):
                birthdateYear = int(birthdate[6:])
                birthdateDay = int(birthdate[0:2])
                birthdateMonth = int(birthdate[3:5])
                #CHECAGEM SE O ANO É VALIDO
                if((birthdateYear < 1944) or (birthdateYear> 2024)):
                    print('Tem certeza que você está vivo?')
                #CHECAGEM SE O MES É VALIDO
                elif((birthdateMonth) <= 0 or (birthdateMonth > 12)):
                    print('Mês digitado inválido')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('Data informada invalida!')
                    elif ((birthdateMonth in thirtyDaysMonth) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in thirtyDaysMonth) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('Data informada invalida!')
                            else:
                                dataCorrect = True
                    else:
                        print('Data informada inválida!')
                else:
                    print('Data informada inválida!')            
            else:
                print('Data informada invalida!')
                
        #CHECAGEM DO EMAIL
        while (True):
            userEmail = input('Informe seu email: ')
            if(userEmail[-4:] == ".com" and (userEmail.count("@") == 1)):
                break
            else:
                print('Email informado errado')
        #CONTROLE DE ADMIN
        while(True):
            id = 0
            checkAdmin = int(input('\033[32mInforme o tipo de cadastro: \n[1] Cliente \n[2] Admin \nOpção: \033[m'))
            if(checkAdmin == 1):
                break
            elif(checkAdmin == 2):
                adminKey = input("Digite a palavra chave para ser admin: ")
                while (True):
                    if(adminKey == "senhafoda123"):
                        id = 1
                        print('Cadastrado como admin!')
                        break
                    else:
                        print("Palavra chave errada!")
                break
            else:
                print('Informe uma opção válida')
                
        age = 2024 - birthdateYear
        usuario['user'] = registerUser
        usuario['password'] = firstPassword
        usuario['age'] = age
        usuario['email'] = userEmail
        usuario['id'] = id
        usuarios.append(usuario.copy())
        
        print('Cadastro concluido com Sucesso!')
        
        
# CRUD - CLIENTE
    if recognized == True:
        for i in usuarios:
            if i['user'] == username:
                if i['id'] == 0:
                    print('Bem vindo ao sistema de clientes!')
                    while True:
                        goBack = int(input('Deseja voltar? \n[1] - Sim \n[2] - Não \nOpção: '))
                        if goBack == 1:
                            recognized = False
                            break
                    
# CRUD - ADMIN
                elif i['id'] == 1:
                    print('Bem vindo ao sistema de admin!')
                    while True:
                        goBack = int(input('Deseja voltar? \n[1] - Sim \n[2] - Não \nOpção: '))
                        if goBack == 1:
                            recognized = False
                            break
    else:
        pass
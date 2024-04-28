monthThirdyDays = [4,6,9,11]
usuarios = list()
usuario = dict()

option = 3

while True:
    
    print('=' * 50 )
    print('CINE SERTÃO'.center(50))
    print('-'.center(50))
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50)

    print('[1] - CATALOGO \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR')

    option = int(input('\033[32mOpção: \033[m'))

    if (option == 3):
        #CONDIÇÃO DE RESET PARA O CADASTRO DO NASCIMENTO
        dataCorrect = False

        registerUser = str(input('Digite o seu nome de usuário: '))
        firstPassword = str(input('Digite a sua senha: '))
        #CHECAGEM DE SENHA
        while True:
            secondPassword = str(input('Confirme a senha: '))
            if(firstPassword == secondPassword):
                break
            else:
                print('A senha esta diferente, digite novamente.')
        #CHECAGEM DA DATA DE NASCIMENTO
        while (dataCorrect != True):

            birthdate = str(input('Digite a data de nascimento [DD/MM/AAAA]: '))
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
                    print('mês digitada invalido')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('Data informada é invalida')
                    elif ((birthdateMonth in monthThirdyDays) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in monthThirdyDays) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('Data informada é invalida')
                            else:
                                dataCorrect = True
                    else:
                        print('Data informada é invalida')
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
                    print('mês digitada invalido')
                #CHECAGEM SE O DIA É VALIDO
                elif((birthdateDay > 0) and (birthdateDay <= 31)):
                    #CHECAGEM DE ANO BISSEXTO
                    if (birthdateDay == 29 and birthdateMonth == 2):
                        if (birthdateYear % 4 == 0 and birthdateYear % 100 != 0) or (birthdateYear % 400 == 0):
                            dataCorrect = True
                        else:
                            print('Data informada é invalida')
                    elif ((birthdateMonth in monthThirdyDays) and birthdateDay < 31):
                            dataCorrect = True
                    elif ((birthdateMonth not in monthThirdyDays) and birthdateDay <= 31):
                            if (birthdateMonth == 2 and birthdateDay > 28):
                                print('Data informada é invalida')
                            else:
                                dataCorrect = True
                    else:
                        print('Data informada é invalida')
                else:
                    print('Data informada invalida')            
            else:
                print('Data informada invalida')
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
            checkAdmin = int(input("Informe o tipo de cadastro: [1] User [2] Admin "))
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
    print('Cadastro concluido com Sucesso!')
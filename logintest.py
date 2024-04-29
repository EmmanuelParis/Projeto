thirdyDaysMonth = [4,6,9,11]
usuarios = list()
usuario = dict()
recognized = False
while True:
    
    print('=' * 50 )
    print('CINE SERTÃO'.center(50))
    print('<--------------->'.center(50))
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50)

    print('[1] - CATÁLOGO \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR')

    option = int(input('\033[32mOpção: \033[m'))
    
    if (option == 2):
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

        usuario['user'] = registerUser
        usuario['password'] = firstPassword
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
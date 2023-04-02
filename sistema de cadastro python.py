#criando as funções utilizadas no menu
def criarcadastro():
    nome = input('Digite seu nome ')
    sobrenome = input('Digite seu sobrenome ')
    email = input('Digite seu email ')
    senha = input('Digite sua senha ')
    logins = open('logins.txt','a')
    logins.write(f'-Nome: {nome} -Sobrenome: {sobrenome} -Email: {email} -senha: {senha} \n')

#menu
while True:
    escolha = input('Escolha uma opção: 1 - criar um cadastro; 2 - sair;')
    if escolha == '1':
        criarcadastro()

    elif escolha == '2':
        print('Obrigada por acessar o site')
        break

    else:
        print('Escolha uma opção valida')

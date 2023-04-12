#criando as funções utilizadas no menu
def criarcadastro():
    nome = input('Digite seu nome ')
    sobrenome = input('Digite seu sobrenome ')
    email = input('Digite seu email ')
    senha = input('Digite sua senha ')
    logins = open('logins.txt','a')
    logins.write(f'-Nome: {nome} -Sobrenome: {sobrenome} -Email: {email} -senha: {senha} \n')

def cadastrarnovo():
    nomeEstabelecimento = input('Digite o nome do estabelecimento')
    locEstabelecimento = input('Digiteo endereço do estabelecimento')
    notaEstabelecimento = int(input(f'Digite uma nota, de 0 a 5, para a acessibilidade dentro do estabelecimento {nomeEstabelecimento}'))
    if notaEstabelecimento >=4:
        int(input('Ficamos felizes em saber disso! Gostaria de compartilhar isso no feed dos seus amigos? Digite 1 para sim e 2 para não'))
    reviewEstabelecimento = input('Escreva uma Review do local para outros usuários')




#menu
while True:
    escolha1 = input('Escolha uma opção: 1 - criar um cadastro; 2 - sair;')
    if escolha1 == '1':
        criarcadastro()
        escolha2 = int(input("Bem vindo ao aplicativo Inclui+! Por onde deseja começar? \n 1- Cadastrar um novo estabelecimento 2- sair "))
        if escolha2 == 1:
            cadastrarnovo()
        elif escolha2 == 2:
            print("Obrigada por se cadastrar no App Inclui+!")
            break
        else:
            print('Por favor escolha uma opção válida')




    elif escolha1 == '2':
        print('Obrigada por acessar o site')
        break

    else:
        print('Escolha uma opção valida')

#funções utilizadas:
#realizando o login:
def criarcadastro():
    nome = input('Digite seu nome ')
    sobrenome = input('Digite seu sobrenome ')
    email = input('Digite seu email ')
    senha = input('Digite sua senha ')
    logins = open('logins.txt','a') #abre um arquivo txt e coloca as informações do usuário
    logins.write(f'-Nome: {nome} -Sobrenome: {sobrenome} -Email: {email} -senha: {senha} \n')
#fazendo a review:
def fazerreview():
    nomeEstabelecimento = input('Digite o nome do estabelecimento')
    locEstabelecimento = input('Digiteo endereço do estabelecimento')
    notaEstabelecimento = int(input(f'Digite uma nota, de 0 a 5, para a acessibilidade dentro do estabelecimento {nomeEstabelecimento}'))
    if notaEstabelecimento >=4: #se a nota for maior que 4, a pessoa pode compartilhar isso com seus amigos do app
        int(input('Ficamos felizes em saber disso! Gostaria de compartilhar isso no feed dos seus amigos? Digite 1 para sim e 2 para não'))
    reviewEstabelecimento = input('Escreva uma Review do local para outros usuários')
#post na comunidade:
def postcomunidade():
    tema = input('Qual o tema central do seu post?')
    post = input('O que você deseja falar?')
    confirmação = input(f'Você deseja mesmo postar isso? Digite s para sim e n para não {post}')
    if confirmação.lower() == 's':
        print('Postagem concluída')
    elif confirmação.lower() == 'n':
        reconfirma = input('Reescreva sua postagem ou aperte 1 para sair')
        if reconfirma != 1:
            print('Postagem concluída')
def cadastrarestabelecimento():
    nomeestabelecimento = input('Digite o nome do seu estabelecimento ')
    cnpj = input('Digite seu CNPJ')
    localização = input('Digite sua localização')
    resenha = input ('faça uma resenha sobre seu estabelecimento')
    estabelecimento = open('estabelecimentos.txt','a') #abre um arquivo txt e coloca as informações do estabelecimento
    estabelecimento.write(f'-Nome: {nomeestabelecimento} -cnpj: {cnpj} -localização: {localização} \n')






print('Seja bem-vindo ao aplicativo Inlui+!')
criarcadastro()
while True:
    menu = int(input('O que você deseja fazer hoje: \n 1- Fazer review de um estabelecimento \n 2- Fazer um post na comunidade \n 3- Cadastrar seu próprio estabelecimento \n 4- sair '))
    match menu:
        case 1:
            fazerreview()
        case 2:
            postcomunidade()
        case 3:
             cadastrarestabelecimento()
        case 4:
            break
        case other:
            print('Digite uma opção válida')

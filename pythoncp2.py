#importando a função exit
from sys import exit

# Função para realizar o cadastro
def criarcadastro():
    nome = input('Digite seu nome: ')  # Solicita o nome do usuário
    sobrenome = input('Digite seu sobrenome: ')  # Solicita o sobrenome do usuário
    email = input('Digite seu email: ')  # Solicita o email do usuário
    senha = input('Digite sua senha: ')  # Solicita a senha do usuário
    
    try:
        with open('logins.txt', 'a') as logins:  # Abre o arquivo 'logins.txt' em modo de escrita
            logins.write(f'-Nome: {nome} -Sobrenome: {sobrenome} -Email: {email} -Senha: {senha}\n')  # Escreve as informações no arquivo
            print('Cadastro realizado com sucesso!')  # Exibe uma mensagem de sucesso
    except IOError:
        print('Erro ao abrir o arquivo de logins.')  # Exibe uma mensagem de erro caso ocorra um problema ao abrir o arquivo
        validação = True

#função para fazer login
def login():
 while True:
        email = input('Digite seu email: ')  # Solicita o email do usuário
        senha = input('Digite sua senha: ')  # Solicita a senha do usuário

        try:
            with open('logins.txt', 'r') as logins:  # Abre o arquivo 'logins.txt' em modo de leitura
                for linha in logins:
                    dados = linha.strip().split(' -') # Separa os valores da linha pelo caractere '-'
                    email_armazenado = dados[2].split(': ')[1] 
                    senha_armazenada = dados[3].split(': ')[1]
                    if email == email_armazenado and senha == senha_armazenada: # Verifica se o email e a senha correspondem aos valores encontrados na linha
                        print('Login realizado com sucesso!')
                        return True 
                print('Email ou senha incorretos. Tente novamente.') # Exibe uma mensagem de boas-vindas
        except IOError:
            print('Erro ao abrir o arquivo de logins.')  # Exibe uma mensagem de erro caso ocorra um problema ao abrir o arquivo
            return False
        else:
            tentar_novamente = input('Deseja tentar novamente? (S/N): ')
            if tentar_novamente.lower() != 's':
                exit()  # Sai do programa se o usuário não quiser tentar novamente

# Função para fazer uma review de um estabelecimento
def fazerreview():
 
    nomeEstabelecimento = input('Digite o nome do estabelecimento: ')  # Solicita o nome do estabelecimento
    locEstabelecimento = input('Digite o endereço do estabelecimento: ')  # Solicita o endereço do estabelecimento
    while True:
        try:
            notaEstabelecimento = int(input(f'Digite uma nota (de 0 a 5) para a acessibilidade dentro do estabelecimento {nomeEstabelecimento}: '))  # Solicita uma nota de acessibilidade ao estabelecimento
            if notaEstabelecimento <= 5:
                compartilhar = input('Ficamos felizes em saber disso! Gostaria de compartilhar isso no feed dos seus amigos? Digite 1 para sim e 2 para não: ')  # Pergunta se o usuário deseja compartilhar a review
                if compartilhar == '1':
                    print('Review compartilhada com sucesso!')  # Exibe uma mensagem de sucesso
                    reviewEstabelecimento = input('Escreva uma review do local para outros usuários: ')  # Solicita uma review do estabelecimento
                break
            else:
                print('Digite um valor válido!')  # Exibe uma mensagem de erro caso a nota seja maior que 5
        except ValueError:
            print('Valor inválido para a nota do estabelecimento.')  # Exibe uma mensagem de erro caso ocorra um problema de conversão de tipo


# Função para fazer um post na comunidade
def postcomunidade():
    tema = input('Qual o tema central do seu post? ')  # Solicita o tema central do post
    post = input('O que você deseja falar? ')  # Solicita o conteúdo do post
    confirmação = input(f'Você deseja mesmo postar isso? Digite "s" para sim e "n" para não: ')  # Pergunta se o usuário deseja postar o conteúdo

    try:
        if confirmação.lower() == 's':  # Verifica se a confirmação é 's' (sim)
            print('Postagem concluída')  # Exibe uma mensagem de sucesso
        elif confirmação.lower() == 'n':  # Verifica se a confirmação é 'n' (não)
            reconfirma = input('Reescreva sua postagem ou aperte 1 para sair: ')  # Pergunta se o usuário deseja reescrever o post ou sair
            if reconfirma != '1':  # Verifica se o usuário digitou algo diferente de '1'
                post = reconfirma  # Atualiza o conteúdo do post com a nova entrada do usuário
                print('Postagem concluída')  # Exibe uma mensagem de sucesso
            else:
                print('Post deletado')  # Exibe uma mensagem informando que o post foi deletado
        else:
            print('Escolha uma resposta válida')
    except ValueError:
        print('Opção inválida.')  # Exibe uma mensagem de erro caso ocorra um problema de conversão de tipo

#função para cadastrar um estabelecimento
def cadastrarestabelecimento():
    nomeestabelecimento = input('Digite o nome do seu estabelecimento: ')  # Solicita o nome do estabelecimento
    while True:
        try:
            cnpj = int(input('Digite seu CNPJ (Digite apenas números): '))  # Solicita o CNPJ do estabelecimento
            break
        except:
            print('Digite um valor válido!')

    localização = input('Digite sua localização: ')  # Solicita a localização do estabelecimento
    resenha = input('Faça uma resenha sobre seu estabelecimento: ')  # Solicita uma resenha sobre o estabelecimento

    try:
        with open('estabelecimentos.txt', 'a') as estabelecimento:  # Abre o arquivo 'estabelecimentos.txt' em modo de escrita
            estabelecimento.write(f'-Nome: {nomeestabelecimento} -CNPJ: {cnpj} -Localização: {localização}\n')  # Escreve as informações no arquivo
            print('Estabelecimento cadastrado com sucesso!')  # Exibe uma mensagem de sucesso
    except IOError:
        print('Erro ao abrir o arquivo de estabelecimentos.')  # Exibe uma mensagem de erro caso ocorra um problema ao abrir o arquivo

print('Seja bem-vindo ao aplicativo Inlui+!')
while True:
    try:
        cadastrooulogin = int(input('Você é novo por aqui? Digite 1 para fazer cadastro e 2 para fazer login '))  # Solicita ao usuário se ele deseja fazer cadastro ou login
        if cadastrooulogin == 1:  # Verifica se a opção é 1 (fazer cadastro)
            criarcadastro()  # Chama a função para realizar o cadastro
            break  # Sai do loop
        elif cadastrooulogin == 2:  # Verifica se a opção é 2 (fazer login)
            login()  # Chama a função para realizar o login
            break  # Sai do loop
        else:
            print('Escolha uma opção valida')  # Exibe uma mensagem de erro para opção inválida
    except ValueError:
        print('Opção inválida')  # Exibe uma mensagem de erro para valor inválido

while True:
    try:
        menu = int(input('O que você deseja fazer hoje:\n1- Fazer review de um estabelecimento\n2- Fazer um post na comunidade\n3- Cadastrar seu próprio estabelecimento\n4- sair\n'))  # Solicita ao usuário a opção desejada no menu
        match menu:  # Avalia a opção selecionada
            case 1:  # Se a opção for 1
                fazerreview()  # Chama a função para fazer uma review de um estabelecimento
            case 2:  # Se a opção for 2
                postcomunidade()  # Chama a função para fazer um post na comunidade

            case 3:  # Se a opção for 3
                cadastrarestabelecimento()  # Chama a função para cadastrar um estabelecimento
            case 4:  # Se a opção for 4
                break  # Sai do loop
            case other:  # Se a opção for diferente das anteriores
                print('Digite uma opção válida')  # Exibe uma mensagem de erro para opção inválida
    except ValueError:
        print('Opção inválida')  # Exibe uma mensagem de erro para valor inválido

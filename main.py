import pickle

def adicionarContato(agenda, nome, email, telefone):
    contato = {'Nome': nome, 'Email': email, 'Telefone': telefone}
    agenda.append(contato)
    print('Contato adicionado com sucesso!')

def listarContatos(agenda):
    if not agenda:
        print('A agenda de contatos está vazia.')
    else:
        print('Lista de contatos:')
        print('------------------')
        for contato in agenda:
            print(f'Nome: {contato["Nome"]}')
            print(f'Email: {contato["Email"]}')
            print(f'Telefone: {contato["Telefone"]}')
            print('------------------')
        input('Pressione Enter para continuar...')

def limparArquivo(arquivo):
    with open(arquivo, 'wb') as file:
        pickle.dump([], file)
    print('Agenda limpa com sucesso!')

def carregarArquivo(arquivo):
    try:
        with open(arquivo, 'rb') as file:
            agenda = pickle.load(file)
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        agenda = []  
    return agenda
    
def salvarContatos(agenda, arquivo):
    with open(arquivo, 'wb') as file:
        pickle.dump(agenda, file)
    print(f'Agenda salva em {arquivo}.')

def listarMenu():
    print('-------- Menu --------')
    print('1- Adicionar contato')
    print('2- Listar contatos')
    print('3- Limpar contatos')
    print('0- Sair')

arquivo = 'arquivo.txt'
lista = carregarArquivo(arquivo)
opcao = 0
while True:
    print('')
    listarMenu()
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            nome      = input('Digite o nome: ')
            email     = input('Digite o email: ')
            telefone  = input('Digite o telefone: ')     
            adicionarContato(lista, nome, email, telefone)       
        case 2:    
            listarContatos(lista)
        case 3:    
            limparArquivo(arquivo)
            lista = []
        case 0:
            salvarContatos(lista, arquivo)
            print('Saindo...')
            break
        case _:
            print('Opção inválida!')
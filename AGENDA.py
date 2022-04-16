#Incluso no Git



AGENDA = {}

AGENDA['Guilherme'] = {
    'tel': '9999-9999',
    'email': 'guilherme@teste',
    'endereco': 'Av 01'
 }


AGENDA['Maria'] = {
    'tel': '9888-9999',
    'email': 'maria@teste',
    'endereco': 'Av 02'
}


def mostrar_Contatos():
            for contato in AGENDA:
                buscar_contato(contato)
                print('----------------------------------------------------------------')

def buscar_contato(contato):
            print("Nome:", contato)
            print("tel:", AGENDA[contato]['tel'])
            print("Email:", AGENDA[contato]['email'])
            print("Endereço:", AGENDA[contato]['endereco'])


def ler_detalhes_contato():
    tel = input('Digite o Telefone: ')
    email = input('Digite o Email: ')
    endereco = input('Digite o Endereço: ')
    return tel, email, endereco



def incluir_editar_contato(contato, tel, email,endereco,):
    AGENDA[contato] = {
        'tel': tel,
        'email': email,
        'endereco': endereco,
        }
    salvar()
    print(">>>>>> Contato {}, e-mail {}, Celular {} adicionado/editado com sucesso <<<<<<".format(contato, email, tel))

def exlcuir_contato(contato):
    AGENDA.pop(contato)
    salvar()
    print(">>>>>> Contato {},  exluído com sucesso. <<<<<<".format(contato))

      

def imprimir_menu():
    print('__________________________________________')
    print("1 - Mostra tosdos os contatos da Agenda")
    print("2 - Buscar contatos da Agenda")
    print("3 - Incluir contatos na Agenda")
    print("4 - Editar contatos da Agenda")
    print("5 - Excluir contatos da Agenda")
    print("6 - Exportar Agenda")
    print("7 - importar Agenda")
    print("0 - Sair da Agenda")
    print('__________________________________________')


def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'tel': tel,
                    'email': email,
                    'endereco': endereco,
                }
              
              
        print('Database carregado com sucesso')
    except FileNotFoundError:
        print('>>> Arquivo não encontrado <<<<<')
    except Exception as error:
        print('>> Algum erro ocorreu ao carregar arquivo<<')
        print(error)


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
               
                incluir_editar_contato(nome, tel,  email, endereco)
    except FileNotFoundError:
        print('>>> Arquivo não encontrado <<<<<')
    except Exception as error:
        print('>> Algum erro ocorreu ao importar arquivo<<')
        print(error)

def exportar_contatos(nome_arquivo):
    try:
            with open(nome_arquivo, 'w') as arquivo:
                ## arquivo.write('nome, tel, email, endereco\n')
                for contato in AGENDA:
                    tel = AGENDA[contato]['tel']
                    email = AGENDA[contato]['email']
                    endereco = AGENDA[contato]['endereco']
                    arquivo.write("{},{},{},{}\n".format(contato, tel, email, endereco))
                    
            print(' >>> Agenda exportada com sucesso')
    except:
            print(' >>> Algum erro ocorreu ao exportar')

## ------------ INICIO DO PROGRAMA DE FATO // ONDE EXECUTA--------------

carregar()

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_Contatos()
    elif opcao =='2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao =='3':
        contato = input('Digite o nome do contato a ser adicionado: ')
        try:
            AGENDA[contato]
            print('Contato já existente')
        except KeyError:
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
           

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>> Editando contado: ', contato)
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
        except KeyError:
            print('Contato inexistente')
    elif opcao =='5':
        contato = input('Digite o nome do contato: ')
        exlcuir_contato(contato)
    elif opcao =='6':
        nome_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_arquivo)
    elif opcao =='7':
        nome_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_arquivo)
    elif opcao =='0':
        print('Fechando')
        break
    else:
        print("Opção inválida")


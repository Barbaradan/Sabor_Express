import os #biblioteca os

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app(): #funtion relacionada ao else
    os.system('cls') #executa o import, cls limpa o terminal
    print('Finalizando o app\n')

def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        match opcao_escolhida: #condição match q substitui if/else
            case 1:
                print('Cadastrar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') #limpa a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
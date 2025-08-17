"""
Projeto de Estudo de caso para prática de Python no curso da Alura.
@date: 2025/08/16
@type: nano project
@author: elss
"""

import os


def apresentacao_principal():
    """ Abertura do programa """
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭━╮╭━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱┃┃╰╯┃┃
┃╰━━┳━━┫╰━┳━━┳━╮┃┃╱╰╋━━┳━━┳━━┳┳━┳━━╮╭━╯┣━━╮┃╭╮╭╮┣━━┳╮╭┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃┃╱╭┫╭╮┃━━┫┃━╋┫╭┫╭╮┃┃╭╮┃╭╮┃┃┃┃┃┃┃╭╮┃╰╯┃╭╮┃┃━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━╯┃╭╮┣━━┃┃━┫┃┃┃╰╯┃┃╰╯┃╭╮┃┃┃┃┃┃┃╭╮┃┃┃┃╭╮┃┃━┫
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┻━━┻━━┻┻╯╰━━╯╰━━┻╯╰╯╰╯╰╯╰┻╯╰┻┻┻┻╯╰┻━━╯""")


def apresentacao_menus():
    """ Apresentando o menu principal """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')


def opcao_invalida():
    print('Opção indevida.')
    print('Voltando ao menu principal.')
    os.system('sleep 2')
    main()


def finalizar_app():
    """ Função de encerramento"""
    os.system('clear')
    print('Obrigado por escolher nossa empresa.')


def menu_opcoes(valor):
    """ Menu de opções """
    try:
        match valor:
            case 1:
                print('Cadastrar Restaurante')
            case 2:
                print('Listar os Restaurantes')
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('clear')
    apresentacao_principal()
    apresentacao_menus()
    menu_opcoes(int(input('Escolha uma opção: ')))


if __name__ == '__main__':
    main()

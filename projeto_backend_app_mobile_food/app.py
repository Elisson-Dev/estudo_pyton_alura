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


def finalizar_app():
    """ Função de encerramento"""
    os.system('clear')
    print('Obrigado por escolher nossa empresa.')


def menu_opcoes(valor):
    """ Menu de opções """
    if (valor == 1):
        print('Cadastrar Restaurante')
    elif (valor == 2):
        print('Listar os Restaurantes')
    elif (valor == 3):
        print('Ativar Restaurante')
    elif (valor == 4):
        finalizar_app()
    else:
        print('Opção indevida. Encerrando o programa')


def main():
    apresentacao_principal()
    apresentacao_menus()
    menu_opcoes(int(input('Escolha uma opção: ')))


if __name__ == '__main__':
    main()

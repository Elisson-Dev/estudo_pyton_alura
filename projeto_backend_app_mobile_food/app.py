"""
Projeto de Estudo de caso para prática de Python no curso da Alura.
@project_name: App Sabor Caseiro da Mamãe
@date: 2025/08/16
@type: nano project
@author: elss
"""

import os

restaurantes = [{'nome': 'Pizza Zé', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Casa Luz', 'categoria': 'Brasileira', 'ativo': True},
                {'nome': 'Lanche KK', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'elss', 'categoria': 'casa', 'ativo': False}
                ]


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


def cadastro_novo_restaurante():
    """ Cadastranto Unidades de Restaurante """
    cabecalho_de_funcoes('Cadastrar')
    nome_restaurante = input('Nome do restaurante a cadastrar: ')
    tipo_restaurante = input('Tipo do restaurante a cadastrar: ')
    dados_restaurante_completo = {'nome': nome_restaurante,
                                  'categoria': tipo_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante_completo)
    voltar_ao_menu_anterior()


def listar_restaurantes():
    """ Listar os Restaurantes Cadastrados """
    cabecalho_de_funcoes('Listar')
    j = 0
    for i in restaurantes:
        j = j+1
        print(f'{j} - {i['nome']} - TIPO: {i['categoria']} - Aberto: {i['ativo']}')
    print('\n')
    voltar_ao_menu_anterior()


def opcao_invalida():
    """ Quando uma Opção for inválida """
    print('Opção indevida.')
    print('Voltando ao menu principal.')
    os.system('sleep 2')
    main()


def finalizar_app():
    """ Função de encerramento"""
    cabecalho_de_funcoes('Finalizar o App')


def menu_opcoes(valor):
    """ Menu de opções """
    try:
        match valor:
            case 1:
                print('Iremos Cadastrar Restaurante')
                os.system('sleep 1')
                cadastro_novo_restaurante()
            case 2:
                print('Iremos listar os Restaurantes')
                os.system('sleep 3')
                listar_restaurantes()
            case 3:
                print('Iremos listar os Restaurantes')
                os.system('sleep 3')
                alterne_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """ Função principal Main() """
    os.system('clear')
    apresentacao_principal()
    apresentacao_menus()
    menu_opcoes(int(input('Escolha uma opção: ')))


def voltar_ao_menu_anterior():
    """ Retorna ao menu principal """
    print('Retornando ao menu anterior. Aguarde...')
    os.system('sleep 2')
    main()


def alterne_estado_restaurante():
    """ Mudar condição de True <-> False """
    cabecalho_de_funcoes('Alternando Estado')
    nome_resturante = input('Qual o restaurante deseja mudar o estado? ')
    for i in restaurantes:
        if (i['nome'] == nome_resturante):
            if (i['ativo'] is True):
                print('Já está ativado e não há o que alterar.')
                os.system('sleep 2')
            else:
                i['ativo'] = True
                print('Agora o Restaurante está Ativo.')
                os.system('sleep 2')
            break
    voltar_ao_menu_anterior()


def cabecalho_de_funcoes(frase):
    """ Inserção de mensagens de cabeçalho de opções """
    os.system('clear')
    print(f'{frase} - Restaurante.')


if __name__ == '__main__':
    main()

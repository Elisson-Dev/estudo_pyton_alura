"""
Projeto de Estudo de caso para prática de Python no curso da Alura.
@date: 2025/08/16
@type: nano project
@author: elss
"""
# Abertura do programa e listagem de menu
print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭━╮╭━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱┃┃╰╯┃┃
┃╰━━┳━━┫╰━┳━━┳━╮┃┃╱╰╋━━┳━━┳━━┳┳━┳━━╮╭━╯┣━━╮┃╭╮╭╮┣━━┳╮╭┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃┃╱╭┫╭╮┃━━┫┃━╋┫╭┫╭╮┃┃╭╮┃╭╮┃┃┃┃┃┃┃╭╮┃╰╯┃╭╮┃┃━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━╯┃╭╮┣━━┃┃━┫┃┃┃╰╯┃┃╰╯┃╭╮┃┃┃┃┃┃┃╭╮┃┃┃┃╭╮┃┃━┫
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┻━━┻━━┻┻╯╰━━╯╰━━┻╯╰╯╰╯╰╯╰┻╯╰┻┻┻┻╯╰┻━━╯""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')

opcao_escolhida = int(input('Escolha uma opção: '))

if (opcao_escolhida == 1):
    print('Cadastrar Restaurante')
elif (opcao_escolhida == 2):
    print('Listar os Restaurantes')
elif (opcao_escolhida == 3):
    print('Ativar Restaurante')
elif (opcao_escolhida == 4):
    print('Obrigado por escolher nossa empresa.')
else:
    print('Opção indevida. Encerrando o programa')

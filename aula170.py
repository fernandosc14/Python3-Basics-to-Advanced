# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# E:\Users\Fernando\Ambiente de Trabalho\Projetos\python\exemplo
# caminho = r'E:\Users\Fernando\Ambiente de Trabalho\Projetos\python\exemplo'
import os

caminho = os.path.join('E:\\', 'Users', 'Fernando', 'Ambiente de Trabalho', 'Projetos', 'python', 'exemplo')

for item in os.listdir(caminho):
    print(item)
    if not os.path.isdir(item):
        continue

    for image in os.listdir(item):
        print('  ',image)

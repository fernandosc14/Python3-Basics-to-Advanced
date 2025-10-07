# os + shutil - Copiando arquivos com Python
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar -> os.unlink
# Apagar pasta recursivamente -> shutil.rmtree

import os
import shutil

HOME = 'E:\\Users\\Fernando'
DESKTOP = os.path.join(HOME, 'Ambiente de Trabalho\\Projetos\\python')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_nova_pasta = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA),
            dir_
        )
        os.makedirs(caminho_nova_pasta, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA),
            file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

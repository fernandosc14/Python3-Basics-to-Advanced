# os.path.getsize e os.stat para dados dos arquivos

import os
import math
from itertools import count

caminho = os.path.join('E:\\', 'Users', 'Fernando', 'Ambiente de Trabalho', 'Projetos', 'python', 'exemplo')
counter = count()

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return '0B'
    
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final}{abreviacao_tamanho}'

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter,'Pasta atual', root)

    for dir_ in dirs:
        print('  ',the_counter,'Diretório', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo_arquivo)
        print('  ',the_counter,'Arquivo', file_, formata_tamanho(tamanho))

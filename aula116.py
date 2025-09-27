import os

"""
Criando arquivos com Python
Usamos a função open() para abrir um arquivo Python
Modos:
r (leitura), w (escrita), a (acrescentar), x (criar), b (binário), t (texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (mover o cursor)
readline (ler uma linha)
readlines (ler várias linhas)

os.remove ou unlink (apagar arquivo)
os.rename (renomear arquivo)

json.dump (escrever json)
json.load (ler json)
"""

caminho = 'aula116.txt'

# arquivo = open(caminho, 'w')
#
# arquivo.close()

# with open(caminho, 'w+', encoding='utf-8') as arquivo:
#     arquivo.write('Linha 1 \n')
#     arquivo.write('Linha 2 \n')
#     arquivo.writelines(
#         ('Linha 3 \n', 'Linha 4 \n')
#     )

#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
    
#     print('Readlines')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha, end='')

# # with open(caminho, 'r') as arquivo:
# #     print(arquivo.read())

with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Linha 2 \n')
    arquivo.writelines(
        ('Linha 3 \n', 'Linha 4 \n')
    )

# os.remove(caminho) # ou unlink
# os.rename(caminho, 'aula116_novo.txt')

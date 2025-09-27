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

# arquivo.close()

with open(caminho, 'w') as arquivo:
    print('Olá mundo!')
    

"""
Entendo os seus próprios módulos
O primeiro módulo executado __main__
Pode importar outro módulo que você criou
O python conhece a pasta onde o __main__
Ele não reconhece pastas e módulos acima do __main__
O python conhece todos os módulos e pacotes nos caminhos do sys.path
"""
import sys
# sys.path.append('/') # Adiciona um novo caminho para o python procurar módulos

import aula97m

print(__name__)
print(*sys.path, sep='\n')

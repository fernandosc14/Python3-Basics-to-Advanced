import importlib # Recarrega o módulo

import aula98m

print(aula98m.var,'\n')

for i in range(10):
    importlib.reload(aula98m)
    print(i)

print('Fim')

#groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Bia', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Daniel', 'nota': 'A'},
    {'nome': 'Rafael', 'nota': 'D'},
    {'nome': 'Gui', 'nota': 'B'},
    {'nome': 'Rebeca', 'nota': 'C'},
    {'nome': 'Pedro', 'nota': 'D'},
    {'nome': 'Gustavo', 'nota': 'A'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

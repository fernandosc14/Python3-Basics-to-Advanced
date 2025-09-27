"""
Exercicio - Lista de tarefas
Comandos: Listar, desfazer, refazer, clear
todo = [] -> Lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café','caminhar'] -> Adicionar caminhar
desfazer = ['fazer café'] -> Remove caminhar
desfazer = [] -> Remove fazer café
refazer = todo ['fazer café'] -> Adiciona fazer café
refazer = todo ['fazer café','caminhar'] -> Adiciona caminhar

Melhoria: Adicionar funções para ações repetitivas
"""
import os
import json

def listar(todo):
    for i, v in enumerate(todo):
        print(i+1, v)
    print()

def adicionar(tarefa, todo, undo):
    todo.append(tarefa)
    if undo:
        undo.clear()
    print()
    listar(todo)
    
def desfazer(todo, undo):
    if not todo:
        print('Nada a desfazer')
        return
    undo.append(todo.pop())
    print()
    listar(todo)

def refazer(todo, undo):
    if not undo:
        print('Nada a refazer')
        return
    todo.append(undo.pop())
    print()
    listar(todo)

def upload(todo, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        save(todo, caminho)
    return dados

def save(todo, caminho):
    dados = todo
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(todo, arquivo, indent=2, ensure_ascii=False)
    return dados

def sair():
    print('Saindo...')
    exit()

def limpar():
    os.system('cls')

caminho = 'aula119.json'
todo = upload([], caminho)
undo = []

while True:
    print('Comandos: listar, desfazer, refazer, limpar, sair')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    comandos = {
        'listar': lambda: listar(todo),
        'adicionar': lambda: adicionar(tarefa, todo, undo),
        'desfazer': lambda: desfazer(todo, undo),
        'refazer': lambda: refazer(todo, undo),
        'limpar': lambda: limpar(),
        'sair': lambda: sair(),
    }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    save(todo, caminho)

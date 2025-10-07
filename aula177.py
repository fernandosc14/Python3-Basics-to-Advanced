# json.dumb e json.load com arquivos

import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

movie = {
    'title': 'O senhor dos Anéis: A Sociedade do Anel', 
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': False, 
    'imdb_rating': 9.8, 
    'year': 2025, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}

with open(CAMINHO_ABSOLUTO, 'w', encoding='utf-8') as arquivo:
    json.dump(movie, arquivo, indent=4, ensure_ascii=False)

with open(CAMINHO_ABSOLUTO, 'r', encoding='utf-8') as arquivo:
    movie_json = json.load(arquivo)
    print(movie_json)

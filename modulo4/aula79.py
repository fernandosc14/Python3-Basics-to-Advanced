# Exercicios - sistemas de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5'
    },
]

total_corretos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}\n')
    print('Opções:')
    for i in range(len(pergunta['Opcoes'])):
        print(f'{i}) {pergunta["Opcoes"][i]}')

    resposta = input('Escolha uma opção: ')
    try:
        if pergunta['Opcoes'][int(resposta)] == pergunta['Resposta']:
            total_corretos += 1
            print('Acertou ✅\n')
        else:   
            print('Errou ❌\n')
    except (ValueError, IndexError):
        print('Errou ❌\n')

print (f'\nAcertou: {total_corretos} de {len(perguntas)} perguntas.')
# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial: https://docs.python.org/3/library/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá, Mundo!"',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Hello World!', # Valor padrão
    required=False,
    # nargs='+', # Recebe um ou mais argumentos
    action='append', # Recebe zero ou mais argumentos
)
args = parser.parse_args()

if args.basic is None:
    print('Use -h ou --help para ajuda.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

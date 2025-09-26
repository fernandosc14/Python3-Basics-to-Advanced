while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+, -, *, /): ")

    num_valido = None

    try:
        num1 = float(num1)
        num2 = float(num2)
        num_valido = True
    except Exception:
        numero_valido = None

    if num_valido is None:
        print("Um dos números digitados não é válido.")
        continue

    operadores_validos = ['+', '-', '*', '/']

    if operador not in operadores_validos:
        print("Operador inválido.")
        continue

    if operador == '+':
        print("Resultado", num1+num2)
    elif operador == '-':
        print("Resultado", num1-num2)
    elif operador == "*":
        print("Resultado", num1*num2)
    elif operador == '/':
        if num2 == 0:
            print("Divisão por zero não é permitida.")
            continue
        print("Resultado", num1/num2)

    sair = input("Deseja sair? (s): ").lower().startswith('s')
    print(sair)

    if sair is True :
        break
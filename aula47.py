import os

palavra = "chefe"
letras_adivinhadas = ''
tentativas = 0

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in palavra:
        letras_adivinhadas += letra

    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letras_adivinhadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    tentativas += 1
    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print("Parabéns! Você adivinhou a palavra.")
        print(f"Você fez {tentativas} tentativas.")
        break
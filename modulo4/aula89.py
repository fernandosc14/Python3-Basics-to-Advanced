# dir, hasattr e getattr em Python
string = "Fernando"
metodo = "upper"

# print(dir(string)) # Mostra todos os atributos e métodos do objeto

if hasattr(string, metodo): # Verifica se o objeto tem o atributo ou método
    print("Existe o método upper")
    print(getattr(string, metodo)()) # Pega o atributo ou método do objeto e executa se for um método
else:
    print("Não existe o método", metodo)

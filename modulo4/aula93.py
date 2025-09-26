# Try, except, else e finally

try:
    a = 1
    b = 0 
    c = a / b
except Exception as e:
    print(e.__class__.__name__) # Mostra o tipo do erro
    print(e) # Mostra o erro

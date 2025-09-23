"""
Excopo de funções Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código pode atingir.
O escopo local é o escopo onde apenas o código dentro de uma função pode atingir.
"""

x = 1

def escopo():
    global x
    x = 10
    def outro():
        y = 100
        print(x,y)
    outro()
    print(x)

print(x)
escopo()
print(x)

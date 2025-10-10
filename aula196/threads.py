from time import sleep
from threading import Thread, Lock

## Usando herança

# class MyThread(Thread):
#     def __init__ (self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
        
#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MyThread('Thread 1 executada', 2)
# t1.start()

# t2 = MyThread('Thread 2 executada', 6)
# t2.start()

# t3 = MyThread('Thread 3 executada', 1)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)

## Usando target e args

# def vai_demorar(texto,tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo!', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo!', 2))
# t3.start()


# for i in range(20):
#     print(i)
#     sleep(.5)

## Usando join para esperar a thread terminar

# def vai_demorar(texto,tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá mundo', 10))
# t1.start()
# t1.join()  # Espera a thread terminar para continuar a execução do código

# # while t1.is_alive():
# #     print('Thread ainda está executando...')
# #     sleep(2)

# print('Thread terminou, agora eu posso continuar')

##

class Tickets:
    def __init__ (self, stock):
        self.stock = stock
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.stock < quantidade:
            print(f'Não temos {quantidade} ingressos disponíveis')
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.stock} ingressos disponíveis')

        self.lock.release()

if __name__ == '__main__':
    tickets = Tickets(10)

    for i in range(1 ,20):
        t = Thread(target=tickets.comprar, args=(i,))
        t.start()

    print(tickets.stock)

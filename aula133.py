"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python não tem modificadores de acesso
Mas podemos seguir as seguintes convenções:
# (sem underline) -> public
# (um underline) -> protected
# (dois underlines) -> private
"""
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'método público'

    def _metodo_protected(self):
        return 'método protegido'

    def __metodo_private(self):
        return 'método privado'

f = Foo()
# print(f.public)
print(f.metodo_publico())
# print(f._metodo_protected())

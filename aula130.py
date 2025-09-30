"""
Method vs @classmethod vs @staticmethod
method - Self, método de instância
@classmethod - cls, método de classe
@staticmethod - sem parâmetro, método estático
"""

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

# c1 = Conection()
c1 = Connection.create_with_auth('admin', '1234')
# c1.set_user('root')
# c1.set_password('1234')

print(c1.__dict__)

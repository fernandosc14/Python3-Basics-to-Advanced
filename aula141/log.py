# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatted = f'{msg} ({self.__class__.__name__})\n'
        print('Salvando no log', msg_formatted)
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatted)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Olá')
    lp.log_success('Sucesso!')

    lf = LogFileMixin()
    lf.log_error('Olá')
    lf.log_success('Sucesso!')

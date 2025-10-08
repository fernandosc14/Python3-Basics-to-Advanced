# Enviando E-mails SMTP com Python

import os
import pathlib
import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv # type: ignore

load_dotenv()

# Caminho html
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados
remetente = os.getenv('FROM_EMAIL', '')
destino = remetente

# Config SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem
with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Fernando')

# Transformar em MIME
mime_multipart = MIMEMultipart()
mime_multipart['From'] = remetente
mime_multipart['To'] = destino
mime_multipart['Subject'] = 'E-mail enviado com Python'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Enviar E-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')

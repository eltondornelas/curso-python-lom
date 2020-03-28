from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart  # para padronizar assunto da mensagem, pra quem, de quem...
from email.mime.text import MIMEText  # recebe o corpo to e-mail que pode ser plain texte ou um texto em html
from email.mime.image import MIMEImage  # recebe a imagem para anexar
import smtplib  # conectar o servidor smtp

meu_email = 'SEUEMAIL@GMAIL.COM'
minha_senha = 'SUASENHA'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Elton Dornelas', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'SEU NOME'
msg['to'] = 'EMAILDOCLIENTE@GMAIL.COM'  # Cliente
msg['subject'] = 'ASSUNTO DO E-MAIL'

corpo = MIMEText(corpo_msg, 'html')
# esse corpo_msg poderia ser um simples texto em string mesmo sem o segundo param, no nosso caso vai ser html
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('imagem.jpg', 'rb') as img:  # rb = read bytes para modo de leitura
#     img = MIMEImage(img.read())
#     msg.attach(img)

# context manager é necessário
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()  # como se fosse um hello
        smtp.starttls()  # questão de segurança do google
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)

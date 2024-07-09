import smtplib
import email.message

def enviar():
    corpo="""
    <p>Teste<p>
    <p>Teste<p>
    """

    msg=email.message.Message()
    msg["Subject"]="Assunto"
    msg["From"]="Remetente"
    msg["To"]="Destinatário"

    #Como Criar a password
        #Gerenciar sua conta/Segurança/Como fazer login no google/Ativar 2 etapas/Senhas do app
    password = "Senha"
   

    msg.add_header("Content-Type","text/html")
    msg.set_payload(corpo)

    s=smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"],password)
    s.sendmail(msg["From"],[msg["To"]],msg.as_string().encode("utf-8"))

    print("Email Enviado")

enviar()
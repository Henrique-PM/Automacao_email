import win32com.client as win32

outlook=win32.Dispatch("outlook.application")
email = outlook.CreateItem(0)

#Configurar as informações:
email.To ="Destinatário"
email.Subject ="Assunto"
email.HTMLBody ="""
<p>Olá é o Paulo<p>
<p>Abs,<p>
<p>TEXTO<p>
<p>oi<p>

"""
#anexo = c:\Users\pmonc\OneDrive\Área de Trabalho\....
#email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")
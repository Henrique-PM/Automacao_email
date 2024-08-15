import win32com.client as win32

outlook=win32.Dispatch("outlook.application")
email = outlook.CreateItem(0)

#Configurar as informações:
email.To ="Destinatário"
email.Subject ="Assunto"
email.HTMLBody ="""
<p>Olá é o Usuário</p>
<p>Abs,</p>
<p>TEXTO</p>
<p>oi</p>

"""
# Adiciona um anexo (se necessário)
# anexo = r'C:\Users\pmonc\OneDrive\Área de Trabalho\seuarquivo.ext'
# email.Attachments.Add(anexo)


email.Send()
print("Email Enviado")

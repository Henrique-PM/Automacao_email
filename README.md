# Envio de E-mails

Este repositório contém dois scripts Python para envio de e-mails:

1. **Envio de e-mails via Gmail usando `smtplib`**
2. **Envio de e-mails via Outlook usando `win32com`**

## Requisitos

Antes de começar, verifique se você possui os seguintes requisitos:

- Python 3.x instalado
- Acesso à Internet
- Uma conta de e-mail (Gmail ou Outlook) configurada

## Script 1: Envio de E-mails via Gmail

### Dependências

Instale a biblioteca necessária para o script usando o seguinte comando:

```bash
pip install secure-smtplib
```

### Configuração

1. **Crie uma Senha de Aplicativo no Gmail:**

   - Vá para [Gerenciar sua conta do Google](https://myaccount.google.com/).
   - Selecione "Segurança" no menu.
   - Na seção "Como fazer login no Google", clique em "Senhas de app".
   - Siga as instruções para criar uma senha de aplicativo específica para o seu script.

2. **Configure o Script:**

   - Abra o arquivo `gmail.py`.
   - Substitua `"Remetente@gmail.com"` com seu endereço de e-mail do Gmail.
   - Substitua `"Destinatário@gmail.com"` com o e-mail do destinatário.
   - Substitua `"Senha"` com a senha de aplicativo gerada.

3. **Execute o Script:**

   ```bash
   python gmail.py
   ```

   O e-mail será enviado e você verá a mensagem "Email Enviado" no console.

## Script 2: Envio de E-mails via Outlook

### Dependências

Certifique-se de que a biblioteca `pywin32` esteja instalada:

```bash
pip install pywin32
```

### Configuração

1. **Configure o Script:**

   - Abra o arquivo `outlook.py`.
   - Substitua `"Destinatario"` com o e-mail do destinatário.

2. **Execute o Script:**

   ```bash
   python outlook.py
   ```

   O e-mail será enviado e você verá a mensagem "Email Enviado" no console.

## Observações

- **Segurança**: Nunca compartilhe suas senhas ou credenciais diretamente em código. Use variáveis de ambiente ou gerenciadores de credenciais seguros.
- **Compatibilidade**: Certifique-se de que o Outlook esteja instalado e configurado corretamente no seu sistema se estiver usando o script do Outlook.
- **Erro de Conexão**: Verifique sua conexão com a Internet e a configuração de firewall se encontrar problemas de conexão.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Abra uma issue ou um pull request para discutir quaisquer alterações.

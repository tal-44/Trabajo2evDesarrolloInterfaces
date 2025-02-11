import smtplib, ssl
from email.message import EmailMessage

def enviarEmailAviso(self, textoError):

        textoEmail = textoError
        # Dirección y contraseña
        email_address = "emisor@emisor.com"
        email_password = "contraseña-emisor"

        # Destinatario
        email_receiver = "receptor@receptor.com"
        # Creación del Mensaje
        msg = EmailMessage()
        msg.set_content(textoEmail)
        msg["Subject"] = "Error Fichajes"
        msg["From"] = email_address
        msg["To"] = email_receiver

        # Servidor SMTP de correo saliente
        smtp_address = "smtp.servidor-emisor.net"
        smtp_port = 587

        context = ssl.create_default_context()

        # Conexión y envío
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context, source_address = email_address) as server:
        with smtplib.SMTP(smtp_address, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(email_address, email_password)
            # server.sendmail(email_address, email_receiver, textoEmail)
            server.send_message(msg)
            server.quit()
        """
        SI EL SERVIDOR ES SMTP_SSL CON UN PUERTO 465 UTILIZAMOS EL SIGUIENTE CÓDIGO
        with smtplib.SMTP_SSL(smtp_address, smtp_port) as server:
            server.login(email_address, email_password)
            # server.sendmail(email_address, email_receiver, textoEmail)
            server.send_message(msg)
            server.quit()
        """
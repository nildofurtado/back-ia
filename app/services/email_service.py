import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings


class EmailService:
    def __init__(self):
        self.smtp_server = settings.SMTP_SERVER
        self.smtp_port = settings.SMTP_PORT
        self.smtp_username = settings.SMTP_USERNAME
        self.smtp_password = settings.SMTP_PASSWORD
        self.email_from = settings.EMAIL_FROM
        self.email_to = settings.EMAIL_TO

    def send_transcription_complete(self, subject: str, body: str):
        message = MIMEMultipart()
        message["From"] = self.email_from
        message["To"] = self.email_to
        message["Subject"] = subject

        message.attach(MIMEText(body, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(message)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def send_password_reset(self, to_email: str, token: str):
        subject = "Redefinição de Senha"
        reset_link = f"https://sua-api/reset-password?token={token}"
        body = f"<p>Clique no link para redefinir sua senha: <a href='{reset_link}'>{reset_link}</a></p>"

        message = MIMEMultipart()
        message["From"] = self.email_from
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(message)
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
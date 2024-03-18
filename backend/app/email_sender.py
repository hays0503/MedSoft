import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server='post.mail.kz', smtp_port=587):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def send_email(self, receiver_email, subject, message):
        # Установка соединения с почтовым сервером
        server = smtplib.SMTP(host=self.smtp_server, port=self.smtp_port)
        server.starttls()
        
        # Вход в учетную запись отправителя
        server.login(self.sender_email, self.sender_password)
        
        # Создание письма
        email_message = MIMEMultipart()
        email_message['From'] = self.sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = subject
        
        # Добавление текста сообщения
        email_message.attach(MIMEText(message, 'plain'))
        
        # Отправка письма
        server.send_message(email_message)
        
        # Закрытие соединения
        server.quit()

# Пример использования
# sender_email = 'MedSoft@mail.kz'
# sender_password = 'i@xngj6GXs8ANPk'

# email_sender = EmailSender(sender_email, sender_password)
# receiver_email = 'hays0503pascal@gmail.com'
# subject = 'Тестовое сообщение'
# message = 'Привет, это тестовое сообщение.'

# email_sender.send_email(receiver_email, subject, message)

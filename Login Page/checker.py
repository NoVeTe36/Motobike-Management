import smtplib
import ssl
from email.message import EmailMessage

class Email:

    def __init__(self):
        self.sender_email = 'tung30062003viet@gmail.com'
        self.sender_password = 'inexjtosdktycubl'

    def send_email(self, user_email):
            # Set the subject and body of the email
            subject = 'Check out my new video!'
            body = """
            I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg
            """

            em = EmailMessage()
            em['From'] = self.sender_email
            em['To'] = user_email
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.sender_email, self.sender_password)
                smtp.sendmail(self.sender_email, user_email, em.as_string())

    def main():
        user_email = input('Enter your email: ')

        email = Email()
        email.send_email(user_email)

if __name__ == '__main__':
    Email.main()
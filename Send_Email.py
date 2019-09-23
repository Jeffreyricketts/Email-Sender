from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASS']
}

app.config.update(mail_settings)
mail = Mail(app)


if __name__=='__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=["rickjeff44@gmail.com"], # replace with recipients email
                        body="This email was sent to you using Pyhton :) ")
        mail.send(msg)
    
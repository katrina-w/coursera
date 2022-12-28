#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate(sender, recipient, subject, body, *attachments):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    for attachement in attachments:
        attachment_path = os.path.basename(attachement)
        mime_type, _ = mimetypes.guess_type(attachement)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachement, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_path)
        
    return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

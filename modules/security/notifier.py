# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_gaia_report(receiver_email, subject, body, attachment_path=None):
    sender_email = "apolo2211@gmail.com"
    app_password = "keyledlixvsjnabb" # Ton code secret 16 caractères

    message = MIMEMultipart()
    message["From"] = f"Gaia-Mind Intelligence <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = f"🛡️ {subject}"
    message.attach(MIMEText(body, "plain"))

    # Gestion de la pièce jointe (Le fameux PDF)
    if attachment_path and os.path.exists(attachment_path):
        filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octat-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            message.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"✅ Rapport envoyé avec succès à {receiver_email}")
    except Exception as e:
        print(f"❌ Erreur Notifier: {e}")
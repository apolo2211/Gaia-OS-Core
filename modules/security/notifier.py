# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gaia_alert(subject, body):
    """
    Système d'alerte mail automatique pour Gaia OS.
    Utilise un mot de passe d'application Google.
    """
    sender_email = "apolo2211@gmail.com"
    receiver_email = "apolo2211@gmail.com"
    # IMPORTANT: Remplace par ton mot de passe d'application Google (16 caractères)
    app_password = "VOTRE_MOT_DE_PASSE_APPLICATION" 

    message = MIMEMultipart()
    message["From"] = f"Gaia OS Shield <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = f"🛡️ [GAIA-CRITICAL] {subject}"

    # Corps du mail
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("✅ Alerte mail envoyée avec succès à l'investigateur Apolo.")
    except Exception as e:
        print(f"❌ Erreur système Notifier: {e}")

if __name__ == "__main__":
    # Test du module
    send_gaia_alert("Système Notifier Actif", "Le module d'alerte de Gaia OS est opérationnel.")
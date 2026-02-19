# -*- coding: utf-8 -*-
from notifier import send_gaia_report
import os

def launch_tesla_mission():
    # TEST : Envoie-le d'abord à toi-même pour vérifier le rendu
    target_email = "apolo2211@gmail.com" 
    subject = "Vulnerability Report: Security Header Misconfiguration - [GAIA-INT-2026]"
    
    body = """Dear Tesla Security Team,

I am Ouerd Seraidi, a security investigator using the Gaia-Mind Intelligence system.

I have identified a security misconfiguration on www.tesla.com regarding missing security headers (CSP and X-Frame-Options), which could lead to UI-redressing/Clickjacking attacks.

Please find the detailed technical report attached to this email. I am available for further technical discussion or demonstration.

Best regards,

Ouerd Seraidi
Lead Security Investigator | Gaia OS Project
Tel: +213 675 13 72 84
Location: Algeria
"""

    pdf_path = "archives/Rapport_Gaia_www_tesla_com.pdf"
    
    if os.path.exists(pdf_path):
        print(f"📧 Sending international security report for Tesla.com...")
        send_gaia_report(target_email, subject, body, pdf_path)
    else:
        print("❌ Error: Tesla PDF not found. Run the generator first!")

if __name__ == "__main__":
    launch_tesla_mission()
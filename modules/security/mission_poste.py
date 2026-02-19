# -*- coding: utf-8 -*-
from notifier import send_gaia_report
import os

def launch_mission():
    target_email = "contact@poste.dz" # Ou ton propre email pour un test final
    subject = "Rapport d'Audit de Sécurité Périmétrique - [GAIA-DZ-2026]"
    
    body = """Monsieur le Responsable technique,

Veuillez trouver ci-joint le rapport d'audit détaillé concernant la sécurité du portail www.poste.dz.
Ce document met en évidence une vulnérabilité de configuration (Clickjacking) impactant la sécurité des usagers.

Le système Gaia-Mind reste à votre disposition pour une démonstration technique.

Cordialement,
Apolo - Lead Security Investigator"""

    pdf_path = "archives/Rapport_Gaia_www_poste_dz.pdf"
    
    if os.path.exists(pdf_path):
        print(f"📧 Préparation de l'envoi du rapport pour Poste.dz...")
        send_gaia_report(target_email, subject, body, pdf_path)
    else:
        print("❌ Erreur : Le fichier PDF est introuvable. Génère-le d'abord !")

if __name__ == "__main__":
    launch_mission()
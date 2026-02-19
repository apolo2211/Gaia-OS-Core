# -*- coding: utf-8 -*-
from notifier import send_gaia_report
import os

def launch_mission():
    # Cible : Poste DZ
    target_email = "contact@poste.dz" 
    subject = "ALERTE SÉCURITÉ : Rapport d'Audit Périmétrique [GAIA-DZ-2026]"
    
    body = """Monsieur le Responsable technique,

Veuillez trouver ci-joint le rapport d'audit détaillé concernant la sécurité du portail www.poste.dz, généré par le sous-système Gaia-Mind.

Cette analyse met en évidence une vulnérabilité critique de type Clickjacking (absence de headers X-Frame-Options) qui expose les usagers à des risques de détournement de session.

Je reste à votre entière disposition pour une démonstration technique ou pour discuter des mesures de remédiation.

Cordialement,

Apolo - Ouerd Seraidi
Lead Security Investigator | Gaia OS Project
Téléphone : +213 675 13 72 84
Localisation : Algérie
"""

    pdf_path = "archives/Rapport_Gaia_www_poste_dz.pdf"
    
    if os.path.exists(pdf_path):
        print(f"📧 Expédition du rapport signé par Ouerd Seraidi...")
        send_gaia_report(target_email, subject, body, pdf_path)
    else:
        print("❌ Erreur : Le fichier PDF est introuvable. Relance 'report_generator.py' d'abord.")

if __name__ == "__main__":
    launch_mission()
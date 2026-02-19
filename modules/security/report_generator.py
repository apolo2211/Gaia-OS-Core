# -*- coding: utf-8 -*-
from fpdf import FPDF
import time
import os

class GaiaPDF(FPDF):
    def header(self):
        # Titre du rapport avec police standard pour éviter les erreurs d'encodage
        self.set_font('Arial', 'B', 15)
        self.set_text_color(0, 102, 204) # Bleu Gaia
        self.cell(0, 10, "GAIA-MIND SECURITY INTELLIGENCE - RAPPORT D'AUDIT", 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Position à 2 cm du bas
        self.set_y(-20)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(100, 100, 100)
        # Signature officielle Ouerd Seraidi
        signature = f"Investigateur : Ouerd Seraidi | Tel : +213 675 13 72 84"
        self.cell(0, 5, signature, 0, 1, 'C')
        self.cell(0, 5, f'Page {self.page_no()} | Gaia-Mind OS Core - Document Officiel', 0, 0, 'C')

def generate_pro_report(target_name, score, findings, lang='FR'):
    # Création du dossier archives s'il n'existe pas
    if not os.path.exists("archives"):
        os.makedirs("archives")

    # Initialisation du PDF
    pdf = GaiaPDF()
    pdf.add_page()
    
    # Infos générales
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    date_label = "Date :" if lang == 'FR' else "Date:"
    target_label = "Cible :" if lang == 'FR' else "Target:"
    pdf.cell(0, 10, f"{date_label} {time.strftime('%d/%m/%Y %H:%M')}", 0, 1)
    pdf.cell(0, 10, f"{target_label} {target_name}", 0, 1)
    
    # Score de sécurité (Cadre de couleur)
    pdf.set_font('Arial', 'B', 14)
    if score < 70:
        pdf.set_text_color(255, 0, 0) # Rouge Danger
    else:
        pdf.set_text_color(0, 128, 0) # Vert Safe
    
    score_text = f"SCORE DE SECURITE GAIA : {score}/100" if lang == 'FR' else f"GAIA SECURITY SCORE: {score}/100"
    pdf.cell(0, 15, score_text, 1, 1, 'C')
    
    # 1. Analyse Technique
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 12)
    title_analysis = "1. Analyse Technique des Failles :" if lang == 'FR' else "1. Technical Findings Analysis:"
    pdf.cell(0, 10, title_analysis, 0, 1)
    
    pdf.set_font('Arial', '', 11)
    # Remplacer les caractères spéciaux par du texte simple pour fpdf (Arial supporte mal certains accents)
    findings_safe = findings.replace('é', 'e').replace('à', 'a').replace('è', 'e').replace('ô', 'o')
    pdf.multi_cell(0, 10, findings_safe)
    
    # 2. Plan de Remédiation
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    title_reco = "2. Plan de Remediation :" if lang == 'FR' else "2. Remediation Plan:"
    pdf.cell(0, 10, title_reco, 0, 1)
    
    pdf.set_font('Courier', '', 10)
    if lang == 'FR':
        reco = "- Ajouter : X-Frame-Options: SAMEORIGIN\n- Configurer : Content-Security-Policy (CSP)\n- Activer : HSTS (Strict-Transport-Security)"
    else:
        reco = "- Add: X-Frame-Options: SAMEORIGIN\n- Setup: Content-Security-Policy (CSP)\n- Enable: HSTS (Strict-Transport-Security)"
    
    pdf.multi_cell(0, 10, reco, 1)

    # Sauvegarde du fichier
    file_name = f"archives/Rapport_Gaia_{target_name.replace('.', '_')}.pdf"
    try:
        pdf.output(file_name)
        print(f"OK : Rapport PDF genere : {file_name}")
    except Exception as e:
        print(f"ERREUR : Impossible de sauvegarder le PDF. Verifiez qu'il n'est pas deja ouvert ! ({e})")

if __name__ == "__main__":
    # Rapport 1 : La Poste
    poste_details = (
        "L'analyse a identifie une absence critique de protection X-Frame-Options. "
        "Le portail de paiement et de consultation CCP est vulnerable au detournement "
        "d'interface, mettant en peril les donnees des citoyens algeriens."
    )
    generate_pro_report("www.poste.dz", 50, poste_details, lang='FR')
    
    # Rapport 2 : Tesla
    tesla_details = (
        "Security audit reveals missing CSP headers on main landing endpoints. "
        "While infrastructure is robust, the lack of UI-redressing protection "
        "on login pages does not meet international security standards."
    )
    generate_pro_report("www.tesla.com", 50, tesla_details, lang='EN')
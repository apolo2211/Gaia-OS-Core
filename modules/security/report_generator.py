# -*- coding: utf-8 -*-
from fpdf import FPDF
import time
import os

class GaiaPDF(FPDF):
    def header(self):
        # Titre du rapport
        self.set_font('Arial', 'B', 15)
        self.set_text_color(0, 102, 204) # Bleu Gaia
        self.cell(0, 10, 'GAIA-MIND SECURITY INTELLIGENCE - RAPPORT D\'AUDIT', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Position à 2 cm du bas
        self.set_y(-20)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(100, 100, 100)
        # Signature officielle Ouerd Seraidi
        self.cell(0, 5, f'Investigateur : Ouerd Seraidi | Tel : +213 675 13 72 84', 0, 1, 'C')
        self.cell(0, 5, f'Page {self.page_no()} | Gaia-Mind OS Core - Document Officiel', 0, 0, 'C')

def generate_pro_report(target_name, score, findings, lang='FR'):
    # Création du dossier archives s'il n'existe pas
    if not os.path.exists("archives"):
        os.makedirs("archives")

    pdf = GaiaPDF()
    pdf.add_page()
    
    # Infos générales
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    date_label = "Date :" if lang == 'FR' else "Date:"
    target_label = "Cible :" if lang == 'FR' else "Target:"
    pdf.cell(0, 10, f"{date_label} {time.strftime('%d/%m/%Y %H:%M')}", 0, 1)
    pdf.cell(0, 10, f"{target_label} {target_name}", 0, 1)
    
    # Score de sécurité
    pdf.set_font('Arial', 'B', 14)
    if score < 70:
        pdf.set_text_color(255, 0, 0) # Rouge Danger
    else:
        pdf.set_text_color(0, 128, 0) # Vert Safe
    
    score_text = f"SCORE DE SECURITE GAIA : {score}/100" if lang == 'FR' else f"GAIA SECURITY SCORE: {score}/100"
    pdf.cell(0, 15, score_text, 1, 1, 'C')
    
    # Analyse Technique
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 12)
    title_analysis = "1. Analyse Technique des Failles :" if lang == 'FR' else "1. Technical Findings Analysis:"
    pdf.cell(0, 10, title_analysis, 0, 1)
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 10, findings)
    
    # Remédiation
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    title_reco = "2. Plan de Remédiation :" if lang == 'FR' else "2. Remediation Plan:"
    pdf.cell(0, 10, title_reco, 0, 1)
    
    pdf.set_font('Courier', '', 10)
    if lang == 'FR':
        reco = "- Ajouter : X-Frame-Options: SAMEORIGIN\n- Configurer : Content-Security-Policy (CSP)\n- Activer : HSTS (Strict-Transport-Security)"
    else:
        reco = "- Add: X-Frame-Options: SAMEORIGIN\n- Setup: Content-Security-Policy (CSP)\n- Enable: HSTS (Strict-Transport-Security)"
    
    pdf.multi_cell(0, 10, reco, 1)

    file_name = f"archives/Rapport_Gaia_{target_name.replace('.', '_')}.pdf"
    pdf.output(file_name)
    print(f"✅ Rapport PDF genere : {file_name}")

if __name__ == "__main__":
    # 1. Rapport pour la Poste (FR)
    generate_pro_report(
        "www.poste.dz", 
        50, 
        "Absence de headers X-Frame-Options detectee. Vulnerabilite critique au Clickjacking. Risque de detournement de session utilisateur.",
        lang='FR'
    )
    
    # 2. Rapport pour Tesla (EN)
    generate_pro_report(
        "www.tesla.com", 
        50, 
        "Missing Content-Security-Policy (CSP) and X-Frame-Options headers. High risk of Clickjacking and UI redressing attacks.",
        lang='EN'
    )
# -*- coding: utf-8 -*-
from fpdf import FPDF
import time
import os

class GaiaPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        # Correction ici : set_text_color au lieu de set_textcolor
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, 'GAIA-MIND SECURITY INTELLIGENCE - RAPPORT D\'AUDIT', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Document Confidentiel - Lead Investigator Apolo', 0, 0, 'C')

def generate_pro_report(target_name, score, findings):
    # Création du dossier archives s'il n'existe pas
    if not os.path.exists("archives"):
        os.makedirs("archives")

    pdf = GaiaPDF()
    pdf.add_page()
    
    # Infos générales
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Date de l'audit : {time.strftime('%d/%m/%Y %H:%M')}", 0, 1)
    pdf.cell(0, 10, f"Cible : {target_name}", 0, 1)
    
    # Score avec couleur
    pdf.set_font('Arial', 'B', 14)
    if score < 70:
        pdf.set_text_color(255, 0, 0) # Rouge pour danger
    else:
        pdf.set_text_color(0, 128, 0) # Vert pour safe
    pdf.cell(0, 15, f"SCORE DE SECURITE GAIA : {score}/100", 1, 1, 'C')
    
    # Corps technique
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "1. Analyse Technique des Failles :", 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 10, findings)
    
    # Recommandations
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "2. Plan de Remédiation :", 0, 1)
    pdf.set_font('Courier', '', 10)
    reco = "Ajouter : X-Frame-Options: SAMEORIGIN\nAjouter : Content-Security-Policy (CSP)\nActiver : HSTS (Strict-Transport-Security)"
    pdf.multi_cell(0, 10, reco, 1)

    file_name = f"archives/Rapport_Gaia_{target_name.replace('.', '_')}.pdf"
    pdf.output(file_name)
    print(f"✅ Rapport PDF genere avec succes : {file_name}")

if __name__ == "__main__":
    # Cibles détectées avec failles
    targets = [
        {
            "name": "www.poste.dz",
            "score": 50,
            "findings": "Absence de headers X-Frame-Options detectee. Vulnerabilite au Clickjacking confirmee. Instabilite DNS sur les noeuds internationaux."
        },
        {
            "name": "www.algerietelecom.dz",
            "score": 50,
            "findings": "Degradation de la configuration de securite. Absence de Content-Security-Policy (CSP). Latence elevee detectee lors des pics de charge."
        }
    ]

    for t in targets:
        generate_pro_report(t["name"], t["score"], t["findings"])
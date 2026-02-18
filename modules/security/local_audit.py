# -*- coding: utf-8 -*-
import requests
import time
import socket
import sys

# Pour forcer le DNS de Google, on utilise parfois la bibliothèque 'dnspython'
# Mais pour rester simple sans installation complexe, on va tenter une résolution directe par socket
# Si la résolution standard échoue, Gaia-Mind signalera l'anomalie.

class LocalDZAudit:
    def __init__(self, log_file):
        self.targets = ["www.entp.dz", "www.algerietelecom.dz", "www.poste.dz"]
        self.log_file = log_file

    def logger(self, message):
        """Affiche dans le terminal et écrit dans le fichier simultanément"""
        print(message)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    def dns_health_check(self, url):
        """Module DNS-Health avec tentative de résolution robuste"""
        host = url.replace("www.", "")
        self.logger(f"🧬 Analyse DNS-Health pour {host}...")
        try:
            # On tente de récupérer l'IP. Si ça échoue, c'est un blocage ou une erreur DNS.
            addr = socket.gethostbyname(host)
            return f"IP: {addr} (Resolution OK)"
        except socket.gaierror:
            self.logger("⚠️ Echec de resolution standard. Tentative via Google DNS (8.8.8.8) simulee...")
            # Note: Pour une vraie requête DNS sortante sur 8.8.8.8 en Python pur, 
            # il faudrait utiliser le port 53. Pour l'instant, on sécurise l'erreur.
            return "ALERTE: Résolution DNS impossible (Blocage probable du FAI)"

    def deep_port_scan(self, url):
        ports = [80, 443, 8080, 21]
        results = {}
        host = url.replace("www.", "")
        self.logger(f"🔍 Gaia-Mind analyse les ports pour {host}...")
        
        try:
            # On vérifie d'abord si le host est résolvable pour éviter le crash Errno 11001
            socket.gethostbyname(host)
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((host, port))
                status = "OUVERT" if result == 0 else "FERME"
                results[port] = status
                sock.close()
        except Exception as e:
            self.logger(f"❌ Scan de ports interrompu pour {host}: Host introuvable.")
            return {p: "INACCESSIBLE" for p in ports}
            
        return results

    def audit_server(self, url):
        self.logger(f"\n🛰️ --- DEBUT DE L'AUDIT GAIA : {url} ---")
        
        # 1. Verification DNS
        dns_status = self.dns_health_check(url)
        self.logger(f"🌐 {dns_status}")

        # 2. Scan de ports (Sécurisé)
        ports = self.deep_port_scan(url)
        self.logger(f"📡 Ports detectes : {ports}")

        # 3. Analyse HTTP/Securite
        try:
            start = time.time()
            # On tente en HTTPS (port 443) car l'ENTP bloque le port 80
            target_url = f"https://{url}"
            # verify=False évite de bloquer sur les certificats SSL auto-signés
            response = requests.get(target_url, timeout=6, verify=False)
            latency = (time.time() - start) * 1000

            security_score = 0
            if response.url.startswith("https"): security_score += 50
            if "X-Frame-Options" in response.headers: security_score += 25
            if "Content-Security-Policy" in response.headers: security_score += 25

            self.logger(f"📊 Latence: {latency:.2f}ms | Score Securite: {security_score}/100")
            
            if security_score < 100:
                self.logger(f"⚠️ Rapport : Manque de Headers de protection (Anti-XSS/Clickjacking).")
                
        except Exception as e:
            self.logger(f"❌ Erreur HTTP : Le serveur sur {url} ne répond pas aux requêtes Gaia.")

if __name__ == "__main__":
    report_path = "audit_report.txt"
    
    # Nettoyage et Entête
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"=== GAIA OS SECURITY REPORT - {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(f"Investigateur : Apolo | Reseau : Starlink/Quantum-Link\n\n")

    auditor = LocalDZAudit(report_path)
    for site in auditor.targets:
        auditor.audit_server(site)
        
    print(f"\n✅ Mission terminee. Resultats sauves dans '{report_path}'.")
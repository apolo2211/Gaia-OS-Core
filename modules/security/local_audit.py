# -*- coding: utf-8 -*-
import requests
import time
import socket
import os

class GaiaGlobalMind:
    def __init__(self):
        # Cibles diversifiées : Algérie + Géants mondiaux
        self.targets = {
            "Algérie": ["www.poste.dz", "www.algerietelecom.dz"],
            "Tech_Giants": ["www.apple.com", "www.google.com", "www.tesla.com"],
            "Infrastructure": ["www.starlink.com"]
        }
        self.archive_dir = "archives"
        if not os.path.exists(self.archive_dir):
            os.makedirs(self.archive_dir)
        
        self.current_report = f"{self.archive_dir}/audit_{int(time.time())}.txt"

    def logger(self, message):
        print(message)
        with open(self.current_report, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    def audit_engine(self):
        self.logger(f"🌍 --- DÉPLOYEMENT GAIA-MIND GLOBAL ---")
        for category, sites in self.targets.items():
            self.logger(f"\n--- CATÉGORIE : {category} ---")
            for url in sites:
                try:
                    start = time.time()
                    # On utilise un User-Agent pour simuler un navigateur et éviter d'être bloqué par Apple/Google
                    headers = {'User-Agent': 'Mozilla/5.0 (Gaia-OS-Alpha)'}
                    r = requests.get(f"https://{url}", timeout=5, headers=headers, verify=False)
                    lat = (time.time() - start) * 1000
                    
                    score = 0
                    if "Content-Security-Policy" in r.headers: score += 50
                    if "Strict-Transport-Security" in r.headers: score += 50
                    
                    self.logger(f"📡 {url} | Latence: {lat:.2f}ms | Score: {score}/100")
                except Exception as e:
                    self.logger(f"❌ {url} : Inatteignable par le noeud actuel.")

if __name__ == "__main__":
    GaiaGlobalMind().audit_engine()
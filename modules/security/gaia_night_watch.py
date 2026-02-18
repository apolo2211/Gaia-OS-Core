# -*- coding: utf-8 -*-
import time
import json
import os
from sub_hunter import hunt_subdomains
from notifier import send_gaia_alert

# Configuration des cibles à haute valeur (2M$+)
TARGETS = ["apple.com", "tesla.com", "google.com"]
DB_FILE = "archives/known_subs.json"

def load_known_subs():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_known_subs(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_nightly_hunt():
    print(f"🌙 Gaia-Mind Night Watch activé à {time.strftime('%H:%M:%S')}")
    known_subs = load_known_subs()
    new_findings = []

    for domain in TARGETS:
        current_subs = hunt_subdomains(domain)
        
        # Initialiser le domaine s'il est nouveau dans notre base
        if domain not in known_subs:
            known_subs[domain] = []

        # Comparaison pour trouver des nouveaux serveurs
        for sub in current_subs:
            if sub not in known_subs[domain]:
                print(f"🔥 NOUVELLE CIBLE DÉTECTÉE : {sub}")
                new_findings.append(sub)
                known_subs[domain].append(sub)

    # Si on trouve quelque chose, on envoie l'alerte mail
    if new_findings:
        subject = "NOUVEAU SERVEUR DÉTECTÉ (Bug Bounty Potential)"
        body = f"Commandant Apolo,\n\nGaia-Mind a détecté de nouveaux sous-domaines actifs :\n\n"
        body += "\n".join([f"- {s}" for s in new_findings])
        body += "\n\nAnalyse recommandée pour recherche de failles."
        send_gaia_alert(subject, body)
        save_known_subs(known_subs)
    else:
        print("    ✅ Aucune nouvelle modification détectée sur les périmètres Apple/Tesla.")

if __name__ == "__main__":
    run_nightly_hunt()
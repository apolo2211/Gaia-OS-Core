# -*- coding: utf-8 -*-
import socket

def hunt_subdomains(domain):
    # Liste étendue avec des cibles à haute sensibilité
    subs = [
        'dev', 'test', 'api', 'vpn', 'staging',        # Classiques
        'payment', 'checkout', 'billing', 'auth',      # Argent & Identité
        'backup', 'db', 'sql', 'archive',              # Données
        'admin', 'portal', 'internal', 'ssh', 'cloud'  # Accès critiques
    ]
    found = []
    print(f"🏹 Gaia-Mind lance la traque profonde sur {domain}...")
    
    for sub in subs:
        target = f"{sub}.{domain}"
        try:
            # Augmentation de la vitesse de résolution
            ip = socket.gethostbyname(target)
            print(f"🎯 CIBLE DÉTECTÉE : {target} -> IP: {ip}")
            found.append(target)
        except socket.gaierror:
            pass
            
    return found
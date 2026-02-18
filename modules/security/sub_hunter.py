# -*- coding: utf-8 -*-
import socket

def hunt_subdomains(domain):
    subs = ['dev', 'test', 'api', 'staff', 'internal', 'staging', 'vpn']
    found = []
    print(f"🏹 Gaia-Mind lance la traque sur {domain}...")
    
    for sub in subs:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            print(f"🎯 CIBLE DÉTECTÉE : {target} -> IP: {ip}")
            found.append(target)
        except socket.gaierror:
            pass # Le sous-domaine n'existe pas
            
    return found

if __name__ == "__main__":
    # Test sur Tesla
    hunt_subdomains("tesla.com")
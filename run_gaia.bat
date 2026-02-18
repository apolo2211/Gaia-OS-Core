@echo off
title GAIA OS - COMMAND CENTER
echo 🚀 Initialisation de Gaia OS Alpha v0.1...
echo 🛰️ Activation du lien Starlink...

:: Lancer le Dashboard dans le navigateur par défaut
start index.html

:: Activer l'environnement Python et lancer l'Audit en arrière-plan
call venv\Scripts\activate
start cmd /k "python modules/security/security_audit_subsystem.py"
start cmd /k "python modules/security/local_audit.py"

echo ✅ Systemes deployes. Surveillez le Dashboard.
pause
@echo off
title GAIA-MIND SECURITY OPERATIONS - Ouerd Seraidi
color 0B

:menu
cls
echo ======================================================
echo           GAIA-MIND INTELLIGENCE SYSTEM
echo        Investigateur : Ouerd Seraidi (+213)
echo ======================================================
echo.
echo  [1] Lancer l'Audit Global (Scan Apple, Tesla, Poste.dz)
echo  [2] Generer les Rapports PDF (Signes Ouerd Seraidi)
echo  [3] Envoyer le Rapport a Poste.dz
echo  [4] Envoyer le Rapport a Tesla.com (Bounty Hunter)
echo  [5] Synchroniser vers GitHub (Sauvegarde Cloud)
echo  [6] Quitter
echo.
echo ======================================================
set /p choice="Selectionnez une option (1-6) > "

if "%choice%"=="1" goto scan
if "%choice%"=="2" goto report
if "%choice%"=="3" goto mission_poste
if "%choice%"=="4" goto mission_tesla
if "%choice%"=="5" goto sync
if "%choice%"=="6" exit
goto menu

:scan
echo [+] Lancement de l'audit perimetrique...
python modules/security/local_audit.py
pause
goto menu

:report
echo [+] Generation des documents PDF officiels...
python modules/security/report_generator.py
pause
goto menu

:mission_poste
echo [+] Envoi du rapport a Poste.dz...
python modules/security/mission_poste.py
pause
goto menu

:mission_tesla
echo [+] Envoi du rapport de test Tesla vers apolo2211@gmail.com...
python modules/security/mission_tesla.py
pause
goto menu

:sync
echo [+] Synchronisation GitHub...
git add .
git commit -m "MAJ Gaia-OS : Automatisation complete"
git push origin main
pause
goto menu
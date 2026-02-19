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
echo  [3] Envoyer le Rapport a Poste.dz (Email Officiel)
echo  [4] Lancer Gaia Night Watch (Surveillance Auto)
echo  [5] Synchroniser vers GitHub (Sauvegarde Cloud)
echo  [6] Quitter
echo.
echo ======================================================
set /p choice="Selectionnez une option (1-6) > "

if %choice%==1 goto scan
if %choice%==2 goto report
if %choice%==3 goto mission
if %choice%==4 goto watch
if %choice%==5 goto sync
if %choice%==6 exit

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

:mission
echo [+] Envoi du rapport signe Ouerd Seraidi a Poste.dz...
python modules/security/mission_poste.py
pause
goto menu

:watch
echo [+] Demarrage de la surveillance nocturne...
python modules/security/gaia_night_watch.py
pause
goto menu

:sync
echo [+] Synchronisation GitHub...
git add .
git commit -m "MAJ Gaia-OS : Audit et Rapports"
git push origin main
pause
goto menu
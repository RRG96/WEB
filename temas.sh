#!/usr/bin/bash

set -e
drush dl aegan -y
drush en aegan -y
drush config-set system.theme default aegan -y
drush config-set system.theme admin aegan -y
rm -f /var/www/sitio1/themes/aegan/logo.png
wget https://www.cert.unam.mx/sites/default/files/banner1.png 
cp banner1.png /var/www/sitio1/themes/aegan/logo.png && rm banner1.png
rm -f /var/www/sitio1/themes/aegan/favicon.ico
wget https://www.seguridad.unam.mx/sites/default/files/logossi_1.png 
cp logossi_1.png /var/www/sitio1/themes/aegan/favicon.ico && rm logossi_1.png
echo "Tema instalado con exito"


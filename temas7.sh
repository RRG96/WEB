#!/bin/sh
set -e
drush dl impact_theme -y
drush en impact_theme -y
drush vset default_theme impact_theme -y
drush vset admin_theme impact_theme -y
rm -f /var/www/sitio1/sites/all/themes/impact_theme/logo.png
wget https://www.cert.unam.mx/sites/default/files/banner1.png 
cp banner1.png /var/www/sitio1/sites/all/themes/impact_theme/logo.png && rm banner1.png
rm -f /var/www/sitio1/sites/all/themes/impact_theme/favicon.ico
wget https://www.seguridad.unam.mx/sites/default/files/logossi_1.png 
cp logossi_1.png /var/www/sitio1/sites/all/themes/impact_theme/favicon.ico && rm logossi_1.png
echo "Tema instalado con exito"

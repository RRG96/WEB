#!/usr/bin/bash

set -e
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
sudo apt-get install php-dom php-zip unzip php-gd php-mbstring -y
sudo ln -s /usr/local/bin/composer /usr/bin/composer
sudo git clone https://github.com/drush-ops/drush.git /usr/local/src/drush
USER=$(whoami)
sudo chown $USER:$USER -R /usr/local/src/drush
cd /usr/local/src/drush
sudo git checkout 8.0.3
sudo ln -s /usr/local/src/drush/drush /usr/bin/drush
composer install
drush --version
echo "Drush instalado correctamente"
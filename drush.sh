<<<<<<< HEAD
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
#composer global require drush/drush
#sudo cat $HOME/.bashrc | grep "PATH" | sed "s/:\\$/:\$HOME\\/.config/composer/vendor/bin/drush:/"
#source $HOME/.bashrc
#drush dl drupal-8.0.3
#mv /var/www/site-blabla/* /var/www/site-blabla.bk
#cp drupal-8.0.3/* /var/www/site-blabla
#rm -rf drupal-8.0.3
echo "Drush instalado correctamente"
=======
#!bin/bash
composer global require drush/drush
sed -i "s/export PATH/$(cat $HOME/.bashrc | grep "PATH" | sed "s-:\$PATH-:\$HOME/.config/composer/vendor/bin/drush:-")/" ~/.bashrc
source $HOME/.bashrc
drush dl drupal-8.0.3
mv /var/www/site-blabla/* /var/www/site-blabla.bk
cp drupal-8.0.3/* /var/www/site-blabla
rm -rf drupal-8.0.3
>>>>>>> 02dbcfb297adef2a50f795bd8baff3be60a32f26

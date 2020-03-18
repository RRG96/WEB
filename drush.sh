#!bin/bash
composer global require drush/drush
sudo cat $HOME/.bashrc | grep "PATH" | sed "s/:\\$/:\$HOME\\/.config/composer/vendor/bin/drush:/"
source $HOME/.bashrc
drush dl drupal-8.0.3
mv /var/www/site-blabla/* /var/www/site-blabla.bk
cp drupal-8.0.3/* /var/www/site-blabla
rm -rf drupal-8.0.3
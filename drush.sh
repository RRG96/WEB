#!bin/bash
composer global require drush/drush
sed -i "s/export PATH/$(cat $HOME/.bashrc | grep "PATH" | sed "s-:\$PATH-:\$HOME/.config/composer/vendor/bin/drush:-")/" ~/.bashrc
source $HOME/.bashrc
drush dl drupal-8.0.3
mv /var/www/site-blabla/* /var/www/site-blabla.bk
cp drupal-8.0.3/* /var/www/site-blabla
rm -rf drupal-8.0.3
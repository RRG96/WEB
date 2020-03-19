#!/bin/bash

apt-get update
apt install php5 php5-pgsql libapache2-mod-php5 php5-gd -y
php drush.phar core-status
chmod +x drush.phar
sudo mv drush.phar /usr/local/bin/drush
drush init -y
cd /var/www
drush dl drupal-7
mv drupal-7.69 sitio2
cp sitio2/sites/default/default.settings.php sitio2/sites/default/settings.php
chown -R www-data:www-data sitio2/
a2enmod ssl
echo "<VirtualHost *:80>
        ServerName magumbos2.unam.local

        Loglevel info

        ServerAdmin magumbocitos@gmail.com
        DocumentRoot /var/www/sitio2

#       RewriteEngine On
#       RewriteCond %{HTTPS} !on
#       RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}


        ErrorLog ${APACHE_LOG_DIR}/sitio2_error.log
        CustomLog ${APACHE_LOG_DIR}/sitio2_access.log combined

</VirtualHost>

<VirtualHost *:443>
        ServerAdmin magumbocitos@gmail.com

        DocumentRoot /var/www/sitio2

        LogLevel info

        ErrorLog ${APACHE_LOG_DIR}/sitio2_error.log
        CustomLog ${APACHE_LOG_DIR}/sitio2_access.log combined

        SSLEngine on

        SSLCertificateFile      /etc/ssl/certs/magumbos.crt
        SSLCertificateKeyFile /etc/ssl/private/magumbos.key

</VirtualHost>" > /etc/apache2/sites-available/sitio2.conf
echo "127.0.0.1 magumbos.unam.local" >> /etc/hosts
a2ensite sitio2.conf
service apache2 restart

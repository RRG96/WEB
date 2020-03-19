#!/usr/bin/python3

from configparser import ConfigParser
import os

config = ConfigParser()
config.read('MIGdrupal.conf')

cadena = (config['Apache']['sitio']).split('.')
cert = (config['SSH']['certPath']).split('/')
key = (config['SSH']['keyPath']).split('/')
if os.system("sudo chmod 777 /var/www/ && cd /var/www/ && drush dl drupal-8 && sudo mv drupal-8.8.4 " + cadena[0] + " && sudo chmod 755 /var/www/ && sudo cp \
    /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/" + cadena[0]  + ".conf") == 0:
    os.system("sudo sshpass -p " + config['SSH']['password'] + " scp " + config['SSH']['user'] + "@" + config['SSH']['ip'] + ":" + config['SSH']['certPath'] + " /etc/ssl/certs/" + cert[len(cert)-1])
    os.system("sudo sshpass -p " + config['SSH']['password'] + " ssh -t " + config['SSH']['user'] + "@" + config['SSH']['ip'] + " \"echo " + config['SSH']['password'] + " | sudo -S chmod 777 " + config['SSH']['keyPath'] + "\"")
    os.system("sudo sshpass -p " + config['SSH']['password'] + " scp " + config['SSH']['user'] + "@" + config['SSH']['ip'] + ":" + config['SSH']['keyPath'] + " /etc/ssl/private/" + key[len(key)-1])
    os.system("sudo sshpass -p " + config['SSH']['password'] + " ssh -t " + config['SSH']['user'] + "@" + config['SSH']['ip'] + " \"echo " + config['SSH']['password'] + " | sudo -S chmod 710 " + config['SSH']['keyPath'] + "\"")
    os.system("sudo sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/" + cadena[0] + "\//g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i 's/\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem/\/etc\/ssl\/certs\/" + cert[len(cert)-1] + "/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i 's/SSLCertificateKeyFile \/etc\/ssl\/private\/ssl-cert-snakeoil.key/SSLCertificateKeyFile \/etc\/ssl\/private\/" + key[len(key)-1] + "/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i 's/{APACHE_LOG_DIR\}\/error.log/{APACHE_LOG_DIR\}\/" + cadena[0] + "-error.log/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i 's/{APACHE_LOG_DIR\}\/access.log/{APACHE_LOG_DIR\}\/" + cadena[0] + "-access.log/g' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i '5 a ServerName " + config['Apache']['sitio'] + "' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i '5 a ServerAlias www." + config['Apache']['sitio'] + "' /etc/apache2/sites-available/" + cadena[0]  + ".conf")
    os.system("sudo sed -i '1 a 127.0.0.1 " + config['Apache']['sitio'] + "' /etc/hosts")
    os.system("sudo a2ensite " + cadena[0]  + ".conf")
    os.system("sudo systemctl restart apache2")

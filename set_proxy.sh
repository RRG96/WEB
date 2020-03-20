#!/usr/bin/bash

set -e
sudo chmod 777 /etc/apache2/sites-available/
sudo cat proxy.conf > /etc/apache2/sites-available/proxy.conf 
sudo a2ensite proxy.conf
sudo systemctl restart apache2
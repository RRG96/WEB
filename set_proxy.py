#!/usr/bin/python3

from configparser import ConfigParser
import os

config = ConfigParser()
config.read('proxy.conf')

os.system("sudo sed -i 's/https:\/\/*.*.*.*/https:\/\/" + config['Proxy']['ipSitio1'] + "\//g' /etc/apache2/sites-available/proxy.conf")
os.system("sudo sed -i '0,/https:\/\/*.*.*.*/! s/https:\/\/*.*.*.*/https:\/\/" + config['Proxy']['ipSitio2'] + "\//' /etc/apache2/sites-available/proxy.conf")

os.system("sudo sed -i 's/ServerName *.*/ServerName " + config['Proxy']['sitio1'] + "/g' /etc/apache2/sites-available/proxy.conf")
os.system("sudo sed -i '0,/ServerName *.*/! s/ServerName *.*/ServerName " + config['Proxy']['sitio2'] + "/' /etc/apache2/sites-available/proxy.conf")

os.system("sudo sed -i 's/ServerAlias www.*/ServerAlias www." + config['Proxy']['sitio1'] + "/g' /etc/apache2/sites-available/proxy.conf")
os.system("sudo sed -i '0,/ServerAlias www.*/! s/ServerAlias www.*/ServerAlias www." + config['Proxy']['sitio2'] + "/' /etc/apache2/sites-available/proxy.conf")

os.system("sudo sed -i '1 a " + config['Proxy']['ipSitio1'] + " " + config['Proxy']['sitio1'] + "' /etc/hosts")
os.system("sudo sed -i '1 a " + config['Proxy']['ipSitio2'] + " " + config['Proxy']['sitio2'] + "' /etc/hosts")